from gantry.logger.utils import _build_batch_iterator
from io import StringIO
import json


def test_build_batch_iterator():
    event_list = [{1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}]
    batch_iter = _build_batch_iterator(event_list, 2)

    result = "".join([part.decode("utf-8") for part in batch_iter])
    file = StringIO(result)

    for line in file.readlines():
        json.loads(line)

    file.seek(0)
    assert len(file.readlines()) == 3
