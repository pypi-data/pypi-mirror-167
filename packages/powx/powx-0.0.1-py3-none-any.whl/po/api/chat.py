from po.core.WeChatType import WeChat
from po.lib.CONST import ACT_TYPE
from po.lib.dec.act_dec import act_info

wx = WeChat()


@act_info(ACT_TYPE.MESSAGE)
def send_message(who, message):
    """
    给指定人，发送一条消息
    :param who:
    :param message:
    :return:
    """

    # 获取会话列表
    wx.GetSessionList()
    wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
    # for i in range(10):
    wx.SendMsg(message)  # 向`文件传输助手`发送消息：你好~
