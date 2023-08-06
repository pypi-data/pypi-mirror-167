## 智慧短信Python SDK说明文档

### 用途
通过SDK提供的函数可直接发起对智慧短信业务的调用，大幅减少为调用能力需提供的代码量。支持HTTP和TCP协议两种方式。
### 如何使用
> pip install sms-tool

#### HTTP
    from smstool import sms_tool
    
    # 向一批号码发送内容相同的短信。accessNumber（虚拟接入码）选填
    sms_tool.http_batch_sms(
        'your account', 
        'your password', 
        ['number1', 'numbern'], 
        'content',
        'accessNumber'
    )
    
    # 点对点批量发送短信。bizId（业务侧id）和accessNumber（虚拟接入码）选填
    sms_tool.http_p2p_sms(
        'your account', 
        'your password',
        [
            {'phoneNumber': 'number1', 'messageContent': 'content1'},
            {'phoneNumber': 'number2', 'messageContent': 'content2', 'bizId': 'bizId2', 'accessNumber': 'accessNumber2'}
        ]
    )
#### TCP
    from smstool import sms_tool

    # CMPP
    待补充

    # SGIP
    待补充

    # SMGP
    待补充

### 目录结构说明
├── smstool                     &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;// sdk实际代码</br>
│   ├── auth                    </br>
│   └── └── auth.py             &emsp;&emsp;&emsp;&emsp;&emsp;// http接口鉴权封装</br>
│   ├── https                   </br>
│   ├── ├── abstract_func.py    &emsp;// http请求抽象封装</br>
│   └── └── api_request.py      &emsp;&emsp;// 后台http接口请求封装</br>
│   ├── utils                   </br>
│   ├── ├── exceptions.py       &emsp;&emsp;// 自定义异常</br>
│   ├── ├── logger.py           &emsp;&emsp;&emsp;&emsp;// 日志类封装</br>
│   └── └── values.py           &emsp;&emsp;&emsp;&emsp;// 常量数据</br>
│   └── sms_tool.py             &emsp;&emsp;&emsp;&emsp;&emsp;// sdk输出文件</br>
├── .gitignore                  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;// git忽略文件</br>
├── LICENSE.txt                 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;// 许可证</br>
├── main.py                     &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;// 程序入口</br>
├── README.md                   &emsp;&emsp;&emsp;&emsp;&emsp;// 工程说明</br>
├── requirements.txt            &emsp;&emsp;&emsp;&emsp;// 依赖列表</br>
└── setup.py                    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;// 打包信息和配置</br>

### 版本记录
- v0.0.1
> 初版