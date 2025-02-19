from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models


# 实例化一个认证对象，入参需要传入腾讯云账户的 SecretId 和 SecretKey
cred = credential.Credential("AKIDSjnkVRBi4CAuUt78wYw8AzTmvscHiwyo", "lJeokV21sWyBCyhEYfbDqIhuysb7Qenj")

# 实例化客户端配置对象
client_profile = ClientProfile()
client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou", client_profile)

# 实例化请求对象
req = models.ChatCompletionsRequest()
req.Model = "hunyuan-standard"
req.Messages = [
    {
        "Role": "user",
        "Content": "请问今天天气如何？"
    }
]

# 发送请求并获取响应
resp = client.ChatCompletions(req)
print(resp.to_json_string())