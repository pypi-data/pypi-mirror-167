from typing import List
import uuid
from promoted_python_delivery_client.client.delivery_request import DeliveryRequest
from promoted_python_delivery_client.model.insertion import Insertion
from promoted_python_delivery_client.model.paging import Paging
from promoted_python_delivery_client.model.response import Response


class SDKDelivery:
    def __init__(self) -> None:
        pass

    def run_delivery(self, request: DeliveryRequest) -> Response:
        req = request.request
        paging = req.paging

        # Set a request id.
        req.request_id = str(uuid.uuid4())
        if paging is None:
            paging = Paging(offset=0, size=len(req.insertion))

        # Adjust size and offset.
        offset = max(0, paging.offset) if paging.offset is not None else 0
        if offset < request.insertion_start:
            raise ValueError("offset should be >= insertion start (specifically, the global position)")
        index = offset - request.insertion_start
        size = paging.size if paging.size is not None else 0
        if size <= 0:
            size = len(req.insertion)

        final_insertion_size = min(size, len(req.insertion) - index)
        insertion_page: List[Insertion] = []
        for i in range(0, final_insertion_size):
            req_ins = req.insertion[index]

            # Delivery response insertions only contain content_id + the fields added in _prepare_response_insertion
            resp_ins = Insertion(content_id=req_ins.content_id)
            self._prepare_response_insertion(resp_ins, offset)
            insertion_page.append(resp_ins)
            index = index + 1
            offset = offset + 1

        return Response(insertion=insertion_page)

    def _prepare_response_insertion(self, ins: Insertion, position: int) -> None:
        ins.position = position
        ins.insertion_id = str(uuid.uuid4())
