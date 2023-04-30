/**
* 图表  echaets d3
*/
var spirit = "image://data:image/png;base64,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";

// 生成自定义象形树状图
function initPictorialBar(opts) {
    let { data, height = 184 } = opts;
    let names = [], values = [];
    // data = [...data, ...data, ...data];
    // data[0].name = "cccccccccccc";
    data.forEach((elem, i) => {
        names.push(elem.name);
        values.push(elem.value);
    })
    const barHeight = 32;
    const fontSize = 15;
    return {
        // backgroundColor: '#000',
        grid: {
            left: '1%',
            right: '12%',
            top: '12%',
            bottom: '3%',
            containLabel: true
        },
        animation: false,
        xAxis: {
            type: 'value',
            show: false,
            // position:"top",
            axisTick: {
                show: false
            },
            axisLabel: {
                show: false
            },
            axisLine: {
                show: false
            },
            splitLine: {
                lineStyle: {
                    type: 'dashed'
                }
            },
        },
        yAxis: {
            show: false,
            axisTick: {
                show: false
            },
            axisLine: {
                lineStyle: {
                    color: '#00D3BC'
                }
            },
            axisLabel: {
                color: '#ddd'
            },
            data: names,
            position: "right"
        },

        series: [
            {
                color: 'rgba(1, 117, 142,0)',
                type: 'pictorialBar',
                symbol: 'rect',

                symbolClip: true,
                symbolRepeat: true,
                symbolSize: [90, barHeight],
                data: values,
                label: {
                    normal: {
                        color: '#fff',
                        show: true,
                        position: "insideLeft",
                        offset: [6, -22],
                        textStyle: {
                            fontSize: fontSize
                        },
                        formatter: function (a, b) {
                            return a.name
                        }
                    }
                }
            },
            {
                color: 'rgba(1, 117, 142,1)',
                type: 'pictorialBar',
                symbol: spirit,
                // barGap:210,
                symbolMargin: "-8%!",
                symbolRepeat: true,
                symbolOffset: ["4%", 0],
                symbolClip: true,
                symbolSize: [85, barHeight],
                data: values,
                label: {
                    show: true,
                    position: 'right',
                    color: "rgb(118,231,230)"
                },
            }
        ]
    };
}

// 生成折线面积图
function initLine(opts) {
    const _colors = [
        '141,253,255',
        '0,188,137',
        '24,129,254',
        '249,67,85',
        '254,187,78',
    ];
    const { names, data } = opts;
    const titles = [];
    const series = [];
    data.forEach((elem, i) => {
        titles.push(elem.name);
        series.push({
            name: elem.name,
            type: 'line',
            smooth: true,
            symbol: 'circle',
            symbolSize: 2,
            showSymbol: false,
            animation: false,
            lineStyle: {
                normal: {
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    //线性渐变，前4个参数分别是x0,y0,x2,y2(范围0~1);相当于图形包围盒中的百分比。如果最后一个参数是‘true’，则该四个值是绝对像素位置。
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: `rgba(${_colors[i]},0.5)`
                    },
                    {
                        offset: 1,
                        color: `rgba(${_colors[i]},0.0)`
                    }
                    ], false),
                    shadowColor: `rgba(${_colors[i]},0.2)`, //阴影颜色
                    shadowBlur: 10 //shadowBlur设图形阴影的模糊大小。配合shadowColor,shadowOffsetX/Y, 设置图形的阴影效果。
                }
            },
            itemStyle: {
                normal: {
                    color: `rgba(${_colors[i]},0.9)`
                },
                emphasis: {
                    color: `rgb(${_colors[i]})`,
                    borderColor: `rgba(${_colors[i]},0.2)`,
                    extraCssText: 'box-shadow: 8px 8px 8px rgba(0, 0, 0, 1);',
                    borderWidth: 10
                }
            },
            data: elem.data
        })
    });
    return {
        backgroundColor: 'transparent',
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                lineStyle: {
                    color: '#aaa'
                }
            }
        },
        legend: {
            icon: 'circle',
            itemWidth: 12,
            itemHeight: 12,
            itemGap: 13,
            data: titles,
            right: '4%',
            textStyle: {
                fontSize: 12,
                color: '#aaa'
            }
        },
        grid: {
            top: 32,
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: [{
            type: 'category',
            boundaryGap: false,
            axisLine: {
                lineStyle: {
                    color: '#aaa'
                }
            },
            data: names
        }],
        yAxis: [{
            type: 'value',
            name: '',
            axisTick: {
                show: false
            },
            axisLine: {
                lineStyle: {
                    color: '#aaa'
                }
            },
            axisLabel: {
                margin: 10,
                textStyle: {
                    fontSize: 12
                }
            },
            splitLine: {
                lineStyle: {
                    color: '#18304f',
                    type: "dashed"
                }
            }
        }],
        series: series
    }
}

//生成饼状图1
function initPie(opts = {}, state = 1) {
    let index = 0;
    var colors = Config.pieColor1;
    var color2 = Config.pieColor2;


    const { data = [] } = opts;
//   console.log(data)
    return {
        tooltip: {
            trigger: 'item'
        },
        animation: false,
        series: [{
            type: 'pie',
            center: ['50%', '50%'],
            radius: ['61%', '79%'],
            itemStyle: {
                normal: {
                    color: "rgba(200,200,200,0.2)"
                }
            },
            data: [0],
            labelLine: {
                normal: {
                    show: false,
                }
            },
            tooltip: {
                show: false
            }
        }, {
            type: 'pie',
            center: ['50%', '50%'],
            radius: ['61%', '79%'],
            clockwise: true,
            avoidLabelOverlap: true,
            hoverOffset: 1,
            itemStyle: {
                normal: {
                    color: function (params) {
                        if (state == 1) {
                            return colors[params.dataIndex]
                        } else if (state == 2) {
                            if (params.name == "高") {
                                return color2[0]
                            } else if (params.name == "中") {
                                return color2[1]
                            } else {
                                return color2[2]
                            }

                        }
                        // return "#5D7092"
                    }
                }
            },
            label: {
                show: true,
                position: 'outside',
                formatter: '{b}：{c}',
                rich: {
                    hr: {
                        backgroundColor: 't',
                        borderRadius: 3,
                        width: 1,
                        height: 1,
                        padding: [1, 1, 0, -1]
                    },
                    a: {
                        padding: [-1, 1, -1, 1]
                    },
                },
                color: "#afb4db"
            },
            labelLine: {
                normal: {
                    length: 3,
                    length2: 3,
                    show: false,
                    lineStyle: {
                        width: 1,
                    }
                }
            },
            data: data
        }]
    };
}

