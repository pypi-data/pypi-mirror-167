from typing import List, Dict, Optional, Generator

from deprecated import deprecated

from annotell.input_api.model.annotation import ExportAnnotation
from annotell.input_api.model.annotation.client_annotation import Annotation, PartialAnnotation
from annotell.input_api.resources.abstract import InputAPIResource
from annotell.input_api.util import filter_none
import urllib

class AnnotationResource(InputAPIResource):

    @deprecated(
        reason="Returns annotations in client-specific format."
        "This method is deprecated in favour of `get_project_annotations` which lets you list "
        "annotations based on project, batch and annotation type."
    )
    def get_annotations(self, input_uuids: List[str]) -> Dict[str, List[ExportAnnotation]]:
        """
        Returns the export ready annotations, either

        :param input_uuids: List with input uuid
        :return Dict: A dictionary containing the ready annotations
        """
        external_id_query_param = ",".join(input_uuids) if input_uuids else None
        json_resp = self._client.get("v1/annotations", params=filter_none({"inputs": external_id_query_param}))

        annotations = dict()
        for k, v in json_resp.items():
            annotations[k] = [ExportAnnotation.from_json(annotation) for annotation in v]
        return annotations

    def get_project_annotations(self, project: str, annotation_type: str, batch: Optional[str] = None) -> Generator[Annotation, None, None]:
        url = f"v1/annotations/projects/{project}/"
        if batch:
            url += f"batch/{batch}/"

        url += f"annotation-type/{annotation_type}/search"

        for js in self._paginate(url):
            partial_annotation = PartialAnnotation.from_json(js)
            content = self._file_client.get_json(partial_annotation.uri)
            yield partial_annotation.to_annotation(content)

    def _paginate(self, base_url: str, next_cursor_id: Optional[int] = None) -> Generator[dict, None, None]:
        next_page_url = urllib.parse.urljoin(base_url, f"?cursorId={next_cursor_id}") if next_cursor_id is not None else base_url
        page = self._client.get(next_page_url)
        for annotation in page.data:
            yield annotation
        if page.metadata.next_cursor_id is not None:
            yield from self._paginate(base_url, page.metadata.next_cursor_id)

    def get_annotation(self, input_uuid: str, annotation_type: str) -> Annotation:
        json_resp = self._client.get(f"v1/annotations/inputs/{input_uuid}/annotation-type/{annotation_type}")
        annotation = Annotation.from_json(json_resp)
        return annotation
