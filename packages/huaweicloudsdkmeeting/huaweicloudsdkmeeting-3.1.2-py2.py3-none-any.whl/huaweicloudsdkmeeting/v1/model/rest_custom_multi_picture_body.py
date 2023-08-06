# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestCustomMultiPictureBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'manual_set': 'int',
        'pic_layout_info': 'PicLayoutInfo',
        'image_type': 'str',
        'subscriber_in_pics': 'list[RestSubscriberInPic]',
        'switch_time': 'int',
        'multi_pic_save_only': 'bool'
    }

    attribute_map = {
        'manual_set': 'manualSet',
        'pic_layout_info': 'picLayoutInfo',
        'image_type': 'imageType',
        'subscriber_in_pics': 'subscriberInPics',
        'switch_time': 'switchTime',
        'multi_pic_save_only': 'multiPicSaveOnly'
    }

    def __init__(self, manual_set=None, pic_layout_info=None, image_type=None, subscriber_in_pics=None, switch_time=None, multi_pic_save_only=None):
        """RestCustomMultiPictureBody

        The model defined in huaweicloud sdk

        :param manual_set: 是否为手工设置多画面： 0： 系统自动多画面 1： 手工设置多画面
        :type manual_set: int
        :param pic_layout_info: 
        :type pic_layout_info: :class:`huaweicloudsdkmeeting.v1.PicLayoutInfo`
        :param image_type: 画面类型
        :type image_type: str
        :param subscriber_in_pics: 子画面列表
        :type subscriber_in_pics: list[:class:`huaweicloudsdkmeeting.v1.RestSubscriberInPic`]
        :param switch_time: 表示轮询间隔，单位：秒。 当同一个子画面中包含有多个视频源时，此参数有效
        :type switch_time: int
        :param multi_pic_save_only: 多画面仅保存
        :type multi_pic_save_only: bool
        """
        
        

        self._manual_set = None
        self._pic_layout_info = None
        self._image_type = None
        self._subscriber_in_pics = None
        self._switch_time = None
        self._multi_pic_save_only = None
        self.discriminator = None

        self.manual_set = manual_set
        if pic_layout_info is not None:
            self.pic_layout_info = pic_layout_info
        if image_type is not None:
            self.image_type = image_type
        if subscriber_in_pics is not None:
            self.subscriber_in_pics = subscriber_in_pics
        if switch_time is not None:
            self.switch_time = switch_time
        if multi_pic_save_only is not None:
            self.multi_pic_save_only = multi_pic_save_only

    @property
    def manual_set(self):
        """Gets the manual_set of this RestCustomMultiPictureBody.

        是否为手工设置多画面： 0： 系统自动多画面 1： 手工设置多画面

        :return: The manual_set of this RestCustomMultiPictureBody.
        :rtype: int
        """
        return self._manual_set

    @manual_set.setter
    def manual_set(self, manual_set):
        """Sets the manual_set of this RestCustomMultiPictureBody.

        是否为手工设置多画面： 0： 系统自动多画面 1： 手工设置多画面

        :param manual_set: The manual_set of this RestCustomMultiPictureBody.
        :type manual_set: int
        """
        self._manual_set = manual_set

    @property
    def pic_layout_info(self):
        """Gets the pic_layout_info of this RestCustomMultiPictureBody.


        :return: The pic_layout_info of this RestCustomMultiPictureBody.
        :rtype: :class:`huaweicloudsdkmeeting.v1.PicLayoutInfo`
        """
        return self._pic_layout_info

    @pic_layout_info.setter
    def pic_layout_info(self, pic_layout_info):
        """Sets the pic_layout_info of this RestCustomMultiPictureBody.


        :param pic_layout_info: The pic_layout_info of this RestCustomMultiPictureBody.
        :type pic_layout_info: :class:`huaweicloudsdkmeeting.v1.PicLayoutInfo`
        """
        self._pic_layout_info = pic_layout_info

    @property
    def image_type(self):
        """Gets the image_type of this RestCustomMultiPictureBody.

        画面类型

        :return: The image_type of this RestCustomMultiPictureBody.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this RestCustomMultiPictureBody.

        画面类型

        :param image_type: The image_type of this RestCustomMultiPictureBody.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def subscriber_in_pics(self):
        """Gets the subscriber_in_pics of this RestCustomMultiPictureBody.

        子画面列表

        :return: The subscriber_in_pics of this RestCustomMultiPictureBody.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.RestSubscriberInPic`]
        """
        return self._subscriber_in_pics

    @subscriber_in_pics.setter
    def subscriber_in_pics(self, subscriber_in_pics):
        """Sets the subscriber_in_pics of this RestCustomMultiPictureBody.

        子画面列表

        :param subscriber_in_pics: The subscriber_in_pics of this RestCustomMultiPictureBody.
        :type subscriber_in_pics: list[:class:`huaweicloudsdkmeeting.v1.RestSubscriberInPic`]
        """
        self._subscriber_in_pics = subscriber_in_pics

    @property
    def switch_time(self):
        """Gets the switch_time of this RestCustomMultiPictureBody.

        表示轮询间隔，单位：秒。 当同一个子画面中包含有多个视频源时，此参数有效

        :return: The switch_time of this RestCustomMultiPictureBody.
        :rtype: int
        """
        return self._switch_time

    @switch_time.setter
    def switch_time(self, switch_time):
        """Sets the switch_time of this RestCustomMultiPictureBody.

        表示轮询间隔，单位：秒。 当同一个子画面中包含有多个视频源时，此参数有效

        :param switch_time: The switch_time of this RestCustomMultiPictureBody.
        :type switch_time: int
        """
        self._switch_time = switch_time

    @property
    def multi_pic_save_only(self):
        """Gets the multi_pic_save_only of this RestCustomMultiPictureBody.

        多画面仅保存

        :return: The multi_pic_save_only of this RestCustomMultiPictureBody.
        :rtype: bool
        """
        return self._multi_pic_save_only

    @multi_pic_save_only.setter
    def multi_pic_save_only(self, multi_pic_save_only):
        """Sets the multi_pic_save_only of this RestCustomMultiPictureBody.

        多画面仅保存

        :param multi_pic_save_only: The multi_pic_save_only of this RestCustomMultiPictureBody.
        :type multi_pic_save_only: bool
        """
        self._multi_pic_save_only = multi_pic_save_only

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RestCustomMultiPictureBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
