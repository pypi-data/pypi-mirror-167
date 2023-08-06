from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from sqlalchemy.dialects import postgresql

from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import exc
from sqlalchemy import select
from sqlalchemy import func


class PgCore:
    """
    Class : PgCore
    """

    def sql_query_to_string(self, engine, query):
        """
        Convert a sqlAlchemy query to the raw sql query (with parameters!)

        :param engine: DB engine
        :type engine: <class 'sqlalchemy.engine.base.Engine'>
        :param query: a sqlAlchemy query
        :type query: class 'sqlalchemy.orm.query.Query'

        :return: the raw sql query
        :rtype: str
        """
        compiled_query = query.statement.compile(
            dialect=postgresql.dialect(),
            compile_kwargs={"literal_binds": True}
        )
        query_mogrified = engine.connect().connection.cursor().mogrify(
            str(compiled_query),
            compiled_query.params
        ).decode()
        return query_mogrified

    def sqlalchemy_connection(self, **kwargs):
        """
        Get the sqlAlchemy session and engine:
        kwargs :
            - "database", "username", "password", "host", "port" (|| +) "scoped_session"
            - "db_url" (|| +) "scoped_session"

        :type database: str
        :type username: str
        :type password: str
        :type host: str
        :type port: int, default 5432
        :type db_url: str

        :return: dict with this following keys session, engine  ; session db and engine db
        :rtype: dict {class 'sqlalchemy.orm.session.Session', <class 'sqlalchemy.engine.base.Engine'>}
        """
        assert {"database", "username", "password", "host", "port"} == set(kwargs.keys()) \
               or {"database", "username", "password", "host", "port", "scoped_session"} == set(kwargs.keys()) \
               or {"db_url"} == set(kwargs.keys()) \
               or {"db_url", "scoped_session"} == set(kwargs.keys())

        # https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine
        client_encoding = "utf8"
        pool_size = 2
        max_overflow = 2
        isolation_level = "AUTOCOMMIT"

        if "db_url" not in kwargs:
            url_db = f"postgresql://{kwargs['username']}:{kwargs['password']}@{kwargs['host']}:{kwargs['port']}/{kwargs['database']}"
        else:
            url_db = kwargs["db_url"]

        engine = create_engine(
            url_db,
            client_encoding=client_encoding,
            executemany_mode="batch",
            pool_size=pool_size,
            max_overflow=max_overflow,
            isolation_level=isolation_level
        )

        if "scoped_session" not in kwargs or not kwargs["scoped_session"]:
            session = sessionmaker(engine)
        else:
            session_factory = sessionmaker(bind=engine)
            session = scoped_session(session_factory)

        return session(), engine

    def _get_metadata(self, engine, schema: str):
        """
        Get DB metadata

        :param engine: DB engine
        :type engine: <class 'sqlalchemy.engine.base.Engine'>
        :param schema: schema name
        :type schema: str

        :return:
        :rtype:
        """
        metadata = MetaData(bind=engine, schema=schema)
        metadata.reflect()
        return metadata

    def table_from_name(self, engine, schema: str, table: str):
        """
        Get a SQL table

        :param engine: DB engine
        :type engine: <class 'sqlalchemy.engine.base.Engine'>
        :param schema: schema name
        :type schema: str
        :param table: table name
        :type table: str

        :return: the sql table
        :rtype: <class 'sqlalchemy.sql.schema.Table'>
        """

        metadata = self._get_metadata(engine, schema)

        try:
            autoload_value = True
            return Table(table, metadata, autoload=autoload_value, autoload_with=engine)

        except exc.NoSuchTableError as _:
            raise ValueError(f"No table {schema}.{table} found!")

    def _is_sql_table_filled(self, engine, schema: str, table: str):
        """
        Check if the sql table is filled

        :param engine: DB engine
        :type engine: <class 'sqlalchemy.engine.base.Engine'>
        :param schema: schema name
        :type schema: str
        :param table: table name
        :type table: str

        :return: filled table ?
        :rtype: bool
        """

        table_found = self.table_from_name(engine, schema, table)
        if table_found is not None:
            rows_count = engine.execute(
                select([func.count()]).select_from(table_found)
            ).scalar()
            if rows_count > 0:
                return True, rows_count

            return True, rows_count

        return None, None
