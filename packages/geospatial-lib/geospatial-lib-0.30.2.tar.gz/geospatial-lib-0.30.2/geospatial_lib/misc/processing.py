from typing import List
from typing import Optional
from typing import Any

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed


def method_processing_modes(processes: List[List], mode: Optional[str] = None, workers_number: int = 4) -> List[Any]:
    """
    To compute multiple methods with Threading, Processing or not
    Warning: to use Processing mode, you have to use the classical main method to run your code


    :param processes: list of list of your methods and their args
    :param mode: processing mode ("threading", "processing", None)
    :param workers_number: number of worker (only for "threading", "processing"
    :return: return function

    """
    assert mode in {"threading", "processing", None}

    if mode == "threading":
        multi_executor_func = ThreadPoolExecutor
    elif mode == "processing":
        multi_executor_func = ProcessPoolExecutor
    else:
        return [
            process[0](*process[1:])
            for process in processes
        ]

    with multi_executor_func(max_workers=workers_number) as executor:

        executions = []
        for process in processes:
            if isinstance(process, list):
                executions.append(executor.submit(*process))
            else:
                executions.append(executor.submit(process))
        return [
            exe.result()
            for exe in as_completed(executions)
        ]
