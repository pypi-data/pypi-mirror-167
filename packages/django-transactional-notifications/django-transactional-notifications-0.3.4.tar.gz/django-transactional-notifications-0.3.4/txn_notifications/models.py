from swapper import swappable_setting

from txn_notifications.base.models import (
    AbstractCategory,
    AbstractTemplate,
    AbstractNotification,
    AbstractUserHandlerSetting,
    AbstractUserCategorySetting,
)


class Category(AbstractCategory):
    class Meta(AbstractCategory.Meta):
        abstract = False
        swappable = swappable_setting("txn_notifications", "Category")


class Template(AbstractTemplate):
    class Meta(AbstractTemplate.Meta):
        abstract = False
        swappable = swappable_setting("txn_notifications", "Template")


class Notification(AbstractNotification):
    class Meta(AbstractNotification.Meta):
        abstract = False
        swappable = swappable_setting("txn_notifications", "Notification")


class UserCategorySetting(AbstractUserCategorySetting):
    class Meta(AbstractUserCategorySetting.Meta):
        abstract = False
        swappable = swappable_setting(
            "txn_notifications", "UserCategorySetting"
        )


class UserHandlerSetting(AbstractUserHandlerSetting):
    class Meta(AbstractUserHandlerSetting.Meta):
        abstract = False
        swappable = swappable_setting(
            "txn_notifications", "UserHandlerSetting"
        )
