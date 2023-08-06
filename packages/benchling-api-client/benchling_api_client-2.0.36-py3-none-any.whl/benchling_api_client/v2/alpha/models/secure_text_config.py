from typing import Any, cast, Dict, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.app_config_item_app_summary import AppConfigItemAppSummary
from ..models.scalar_config_types import ScalarConfigTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecureTextConfig")


@attr.s(auto_attribs=True, repr=False)
class SecureTextConfig:
    """  """

    _description: Union[Unset, None, str] = UNSET
    _name: Union[Unset, str] = UNSET
    _required_config: Union[Unset, bool] = False
    _type: Union[Unset, ScalarConfigTypes] = UNSET
    _value: Union[Unset, None, str] = UNSET
    _app: Union[Unset, AppConfigItemAppSummary] = UNSET
    _app_id: Union[Unset, str] = UNSET
    _api_url: Union[Unset, str] = UNSET
    _id: Union[Unset, str] = UNSET
    _modified_at: Union[Unset, str] = UNSET

    def __repr__(self):
        fields = []
        fields.append("description={}".format(repr(self._description)))
        fields.append("name={}".format(repr(self._name)))
        fields.append("required_config={}".format(repr(self._required_config)))
        fields.append("type={}".format(repr(self._type)))
        fields.append("value={}".format(repr(self._value)))
        fields.append("app={}".format(repr(self._app)))
        fields.append("app_id={}".format(repr(self._app_id)))
        fields.append("api_url={}".format(repr(self._api_url)))
        fields.append("id={}".format(repr(self._id)))
        fields.append("modified_at={}".format(repr(self._modified_at)))
        return "SecureTextConfig({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        description = self._description
        name = self._name
        required_config = self._required_config
        type: Union[Unset, int] = UNSET
        if not isinstance(self._type, Unset):
            type = self._type.value

        value = self._value
        app: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self._app, Unset):
            app = self._app.to_dict()

        app_id = self._app_id
        api_url = self._api_url
        id = self._id
        modified_at = self._modified_at

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if required_config is not UNSET:
            field_dict["requiredConfig"] = required_config
        if type is not UNSET:
            field_dict["type"] = type
        if value is not UNSET:
            field_dict["value"] = value
        if app is not UNSET:
            field_dict["app"] = app
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if api_url is not UNSET:
            field_dict["apiUrl"] = api_url
        if id is not UNSET:
            field_dict["id"] = id
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def get_description() -> Union[Unset, None, str]:
            description = d.pop("description")
            return description

        description = get_description() if "description" in d else cast(Union[Unset, None, str], UNSET)

        def get_name() -> Union[Unset, str]:
            name = d.pop("name")
            return name

        name = get_name() if "name" in d else cast(Union[Unset, str], UNSET)

        def get_required_config() -> Union[Unset, bool]:
            required_config = d.pop("requiredConfig")
            return required_config

        required_config = get_required_config() if "requiredConfig" in d else cast(Union[Unset, bool], UNSET)

        def get_type() -> Union[Unset, ScalarConfigTypes]:
            type = None
            _type = d.pop("type")
            if _type is not None and _type is not UNSET:
                try:
                    type = ScalarConfigTypes(_type)
                except ValueError:
                    type = ScalarConfigTypes.of_unknown(_type)

            return type

        type = get_type() if "type" in d else cast(Union[Unset, ScalarConfigTypes], UNSET)

        def get_value() -> Union[Unset, None, str]:
            value = d.pop("value")
            return value

        value = get_value() if "value" in d else cast(Union[Unset, None, str], UNSET)

        def get_app() -> Union[Unset, AppConfigItemAppSummary]:
            app: Union[Unset, AppConfigItemAppSummary] = UNSET
            _app = d.pop("app")
            if not isinstance(_app, Unset):
                app = AppConfigItemAppSummary.from_dict(_app)

            return app

        app = get_app() if "app" in d else cast(Union[Unset, AppConfigItemAppSummary], UNSET)

        def get_app_id() -> Union[Unset, str]:
            app_id = d.pop("appId")
            return app_id

        app_id = get_app_id() if "appId" in d else cast(Union[Unset, str], UNSET)

        def get_api_url() -> Union[Unset, str]:
            api_url = d.pop("apiUrl")
            return api_url

        api_url = get_api_url() if "apiUrl" in d else cast(Union[Unset, str], UNSET)

        def get_id() -> Union[Unset, str]:
            id = d.pop("id")
            return id

        id = get_id() if "id" in d else cast(Union[Unset, str], UNSET)

        def get_modified_at() -> Union[Unset, str]:
            modified_at = d.pop("modifiedAt")
            return modified_at

        modified_at = get_modified_at() if "modifiedAt" in d else cast(Union[Unset, str], UNSET)

        secure_text_config = cls(
            description=description,
            name=name,
            required_config=required_config,
            type=type,
            value=value,
            app=app,
            app_id=app_id,
            api_url=api_url,
            id=id,
            modified_at=modified_at,
        )

        return secure_text_config

    @property
    def description(self) -> Optional[str]:
        if isinstance(self._description, Unset):
            raise NotPresentError(self, "description")
        return self._description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        self._description = value

    @description.deleter
    def description(self) -> None:
        self._description = UNSET

    @property
    def name(self) -> str:
        if isinstance(self._name, Unset):
            raise NotPresentError(self, "name")
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @name.deleter
    def name(self) -> None:
        self._name = UNSET

    @property
    def required_config(self) -> bool:
        if isinstance(self._required_config, Unset):
            raise NotPresentError(self, "required_config")
        return self._required_config

    @required_config.setter
    def required_config(self, value: bool) -> None:
        self._required_config = value

    @required_config.deleter
    def required_config(self) -> None:
        self._required_config = UNSET

    @property
    def type(self) -> ScalarConfigTypes:
        if isinstance(self._type, Unset):
            raise NotPresentError(self, "type")
        return self._type

    @type.setter
    def type(self, value: ScalarConfigTypes) -> None:
        self._type = value

    @type.deleter
    def type(self) -> None:
        self._type = UNSET

    @property
    def value(self) -> Optional[str]:
        if isinstance(self._value, Unset):
            raise NotPresentError(self, "value")
        return self._value

    @value.setter
    def value(self, value: Optional[str]) -> None:
        self._value = value

    @value.deleter
    def value(self) -> None:
        self._value = UNSET

    @property
    def app(self) -> AppConfigItemAppSummary:
        if isinstance(self._app, Unset):
            raise NotPresentError(self, "app")
        return self._app

    @app.setter
    def app(self, value: AppConfigItemAppSummary) -> None:
        self._app = value

    @app.deleter
    def app(self) -> None:
        self._app = UNSET

    @property
    def app_id(self) -> str:
        """ The id of a Benchling app """
        if isinstance(self._app_id, Unset):
            raise NotPresentError(self, "app_id")
        return self._app_id

    @app_id.setter
    def app_id(self, value: str) -> None:
        self._app_id = value

    @app_id.deleter
    def app_id(self) -> None:
        self._app_id = UNSET

    @property
    def api_url(self) -> str:
        if isinstance(self._api_url, Unset):
            raise NotPresentError(self, "api_url")
        return self._api_url

    @api_url.setter
    def api_url(self, value: str) -> None:
        self._api_url = value

    @api_url.deleter
    def api_url(self) -> None:
        self._api_url = UNSET

    @property
    def id(self) -> str:
        if isinstance(self._id, Unset):
            raise NotPresentError(self, "id")
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    @id.deleter
    def id(self) -> None:
        self._id = UNSET

    @property
    def modified_at(self) -> str:
        """ DateTime the template was last modified """
        if isinstance(self._modified_at, Unset):
            raise NotPresentError(self, "modified_at")
        return self._modified_at

    @modified_at.setter
    def modified_at(self, value: str) -> None:
        self._modified_at = value

    @modified_at.deleter
    def modified_at(self) -> None:
        self._modified_at = UNSET
