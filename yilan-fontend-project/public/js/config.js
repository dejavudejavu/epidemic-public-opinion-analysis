/**
* 页面参数配置
*/
{
    const bottomBasic = [
        {
            name: "言论",
            style: {
                flex: 1,
            }
        },
        {
            name: "发布时间",
            style: {
                flex: 1
            }
        },
        {
            name: "置信度",
            style: {
                flex: 1
            }
        },
        {
            name: "系统判定",
            style: {
                flex: 1
            }
        },
        {
            name: "来源",
            style: {
                flex: 1
            }
        },
        // {
        //     name: "攻击类型",
        //     style: {
        //         flex: 1
        //     }
        // },
        // {
        //     name: "攻击位置",
        //     style: {
        //         flex: 1
        //     }
        // },
        // {
        //     name: "攻击IP",
        //     style: {
        //         flex: 1
        //     }
        // },
        // {
        //     name: "时间",
        //     style: {
        //         flex: 1
        //     }
        // },
    ];

    const textConfig = {
        // head
        title: "新冠舆情分析平台"
        // center
        // bottom
    };

    const pieColor1 = [
        '#447acf',
        '#46ae86',
        '#465d78',
        '#bd991c',
        '#b05740',
        '#b05740',
        '#54a3bf',
        '#7c69b6',
        '#7c69b6',
        '#e09958',
        '#1b8284',
        '#ea9bc5',
    ];

    const pieColor2 = [
        "#FF5050",
        "#FFB341",
        "#FFE783"
    ];

    const dayConfig = [
        {
            value: 7
        }, {
            value: 15
        }, {
            value: 30
        }, {
            value: 90
        }
    ]

    window.Config = {
        text: textConfig,
        color: {},
        bottomBasic,
        pieColor1,
        pieColor2,
        dataTime: 550000,// 数据时间
        listTime: 1000, // 列表更新事件
        carTime: 60000, // 车型更新时间
        dayConfig: dayConfig,
        isAlert: true,
        alertTime: 5000, // 存在时间
        alertText: function (num = 1) {
            return `发生了${num}次安全事件`
        }
    }
}
