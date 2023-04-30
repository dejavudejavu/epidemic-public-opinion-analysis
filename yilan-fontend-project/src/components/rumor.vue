<template>
    <div class="c-mains c-m-box" style="top: 112px">
        <div class="c-m-flex-2 c-m-flex;" style="margin-right: 30px">
            <c-box style="width: 100%; height: 100%">
                <template v-slot:main>
                    <div class="c-list-head headtext" style="padding-left: 0">
                        <div style="text-align: center"  class="c-l-title">
                            <span>谣言量变化趋势</span>
                        </div>
                    </div>
                    <div class="full-box" id="chart0"></div>
                </template>
            </c-box>
        </div>
        <div class="c-m-flex-1 c-m-flex">
            <c-box style="width: 100%; height: 49%">
                <template v-slot:main>
                    <div class="c-list-head headtext" style="padding-left: 0">
                        <img
                            src="../../public/images/chartbg_head.png"
                            style="float: left; margin-top: 2px"
                        />                             
                        <div style="text-align: center"  class="color-title">
                             谣言高频词                            
                        </div>
                    </div>
                    <div class="full-box" id="chart1"></div>
                </template>
            </c-box>
            <c-box style="width: 100%; height: 49%; margin-top:2%">
                <template v-slot:main>
                    <div class="c-list-head headtext" style="padding-left: 0">
                        <img
                            src="../../public/images/chartbg_head.png"
                            style="float: left; margin-top: 2px"
                        />                             
                        <div style="text-align: center" class="color-title">
                            谣言词云图
                        </div>
                    </div> 
                    <div class="c-list-main full-box" id='ciyun'>   
                         <img src="http://159.75.23.139:3000/yilan-json/rumor/wordcloud.png" style="width:100%; height:100%"/>                
                    </div>                                                         
                </template>
                     
            </c-box> 
        </div>
    </div>
</template>

<script scoped>
export default {
    data() {
        return {
                texts: {
                title: "新冠",
            },
            attackType: 1,
            eventTotals: [],
            deviceTotals: [],
            leftState: 1,
            leftData: [
                {
                    name: "谣言量变化趋势",
                    value: 0,
                    unit: "次",
                },
            ],
        };
    },
    mounted() {
        this.yaoyan();
        this.mentioned();
    },
    methods: {
        //谣言量变化趋势
        yaoyan() {
            var chartDom = document.getElementById("chart0");
            var myChart = this.$echarts.init(chartDom);
            this.axios.get(this.baseUrl+'/yilan-json/rumor/RumorChange.json').then((res)=>{
                
                var tempdata=res.data
                // var value=res.data.value
                var data=[]
                for(var i=0;i<tempdata.length; i++){
                    var id=parseInt(tempdata[i].time.substring(tempdata[i].time.length - 4).replace(/\./,""))
                    var item={
                        time:tempdata[i].time,
                        num:tempdata[i].num,
                        id:id
                    }
                    data.push(item)
                }
                data.sort(function(a,b){
                    return a.id - b.id
                })
                // 
                let xData = [], yData = []
                data.map(v => {
                    xData.push(v.time)
                    yData.push(v.num)
                })
                option = {
                    backgroundColor: 'rgba(1,42,53,0.8)',
                    grid: {
                        top: '5%',
                        right: '5%',
                        left: '5%',
                        bottom: '10%'
                    },                
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            label: {
                                backgroundColor: '#6a7985',
                                fontSize: 12
                            },
                        },
                        textStyle: { fontSize: '100%' },
                        formatter: v => {
                            return `
                            <div class='u-p-2'>
                                <div class='fz-10'>日期：${v[0].axisValue}</div>
                                <div class='fz-10 u-mt-2'>谣言数：${v[0].value}</div>
                            </div>
                            `
                        }
                    },
                    xAxis: {
                        type: 'category', boundaryGap: false, // 两边留白
                        axisLabel: { textStyle: { color: '#fff', fontSize:14}},
                        data: xData,
                        axisLine: { lineStyle: { color:'#000', width:1}},    
                        splitLine: { lineStyle: { type: 'dashed', color: 'rgba(255,255,255,.2)',width:1}, show: true },
                    },
                    yAxis:{ 
                        name:'条', type: 'value', scale: true, 
                        nameTextStyle: { color:'rgba(255,255,255,.5)', align:'right', padding:[0,10,0,0], fontSize: '100%'},
                        axisLabel: { textStyle: { color: '#fff', fontSize: '100%' }, margin: 8 }, 
                        axisLine: { lineStyle: { color:'#000', width:1 }},    
                        splitLine: { lineStyle: { type: 'solid', color: 'rgba(255,255,255,.2)',width:1 }, show: true }
                    },
                    dataZoom: [{
                        show: true,
                        height: "3%",
                        xAxisIndex: [0],
                        bottom: "3%",
                        "start": 10,
                        "end": 80,
                        handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
                        handleSize: '110%',
                        handleStyle: {
                            color: "#5B3AAE",
                        },
                        textStyle:{
                            color:"rgba(204,187,225,0.5)",
                        },
                        fillerColor:"#3a76f6",
                        borderColor: "rgba(204,187,225,0.5)",

                    }, 
                    {
                        type: "inside",
                        show: true,
                        height: 15,
                        start: 1,
                        end: 35
                    }],                     
                    series: {
                        name: '', type: 'line', stack: '',
                        // 修改的是线下区域的颜色
                        areaStyle: { color:  new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(236, 99, 123, .5)'
                        }, {
                            offset: 1,
                            color: 'rgba(102, 212, 250,.0)'
                        }])},
                        // 修改的是线的颜色
                        lineStyle: { color: { 
                            type: 'linear',x: 0, y: 1, x2: 0, y2: 0,
                            // 0% 处的颜色                           // 100% 处的颜色
                            colorStops: [{ offset: 0, color: '#3a76f6' },{ offset: .25, color: '#66d4fa' }, { offset: .75, color: '#f8d470'}, { offset: 1, color: '#ec637b'}],
                            global: false // 缺省为 false
                        },width:2},
                        //图例样式，默认空心圆，设为none是实心，还有'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
                        symbol:'none',  
                        data: yData,
                        markLine: {
                            // symbol: 'none',
                            data: [{
                                type:'max',
                                name: "谣言最高峰",
                                // xAxis: '2-17',
                                lineStyle: {
                                    color: '#eb6272',
                                    type: "dashed",
                                    width: 1
                                },
                                label: { 
                                    show: true, formatter: '谣言最高峰\n{a|}',
                                    align:'center',
                                    distance: [0,-60],
                                    fontSize: 14,
                                    rich: { 
                                        // a:{ backgroundColor: { image: bg1 }, width: 20, height: 20 }
                                    }
                                }
                            }]
                        }
                    }
                };
                option && myChart.setOption(option);   
            })            
            var option;
                    
        },
        mentioned() {
            var chartDom = document.getElementById("chart1");
            var myChart = this.$echarts.init(chartDom);
            this.axios.get(this.baseUrl+'/yilan-json/rumor/RumorSub.json').then((res)=>{
                var temp = res.data
                var data={
                    words:temp.words.slice(0,7),
                    value:temp.value.slice(0,7),
                    sentence:temp.sentence.slice(0,7)
                }
                var option;
                option = {
                    backgroundColor: 'rgba(1,42,53,0.8)',
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        },
                        formatter:v=> {
                                var id=v[0].dataIndex
                                                                
                                return `
                                    <div class='u-p-2' style='width:400px'>
                                        <div style='font-weight: bold;font-size:20px'><span style="color:#3CDDCF">●</span>${data.words[id]}</div>
                                        <div class='fz-10'>次数：${data.value[id]}</div>
                                        <div class='fz-10 u-mt-2' style='white-space:normal; word-break:break-all;overflow:hidden;'>代表谣言：${data.sentence[id]}</div>
                                    </div>                                        
                                `
                        },                          
                    },
                    grid: {
                        bottom: '10%'
                    },
                    xAxis: [{
                        type: 'category',
                        data: data.words,
                        axisLine: {
                            lineStyle: {
                                color: 'rgba(255,255,255,0.12)'
                            }
                        },
                        axisLabel: {
                            color: '#e2e9ff',
                            textStyle: {
                                fontSize: 14
                            },
                        },
                    }],
                    yAxis: [{
                        name: '单位：次',
                        axisLabel: {
                            formatter: '{value}',
                            color: '#e2e9ff',
                        },
                        axisLine: {
                            show: false,
                            lineStyle: {
                                color: 'rgba(255,255,255,1)'
                            }
                        },
                        splitLine: {
                            lineStyle: {
                                color: 'rgba(255,255,255,0.12)'
                            }
                        }
                    }],
                    series: [{
                        type: 'bar',
                        data:data.value,
                        barWidth: '20px',
                        itemStyle: {
                            normal: {
                                color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                    offset: 0,
                                    color: 'rgba(0,244,255,1)' // 0% 处的颜色
                                }, {
                                    offset: 1,
                                    color: 'rgba(0,77,167,1)' // 100% 处的颜色
                                }], false),
                                barBorderRadius: [30, 30, 30, 30],
                                shadowColor: 'rgba(0,160,221,1)',
                                shadowBlur: 4,
                            }
                        },
                        label: {
                            normal: {
                                show: false,
                                lineHeight: 30,
                                width: 80,
                                height: 30,
                                backgroundColor: 'rgba(0,160,221,0.1)',
                                borderRadius: 200,
                                position: ['-8', '-60'],
                                distance: 1,
                                // formatter: [
                                //     '    {d|●}',
                                //     ' {a|{c}}     \n',
                                //     '    {b|}'
                                // ].join(','),
                              
                                rich: {
                                    d: {
                                        color: '#3CDDCF',
                                    },
                                    a: {
                                        color: '#fff',
                                        align: 'center',
                                    },
                                    b: {
                                        width: 1,
                                        height: 30,
                                        borderWidth: 1,
                                        borderColor: '#234e6c',
                                        align: 'left'
                                    },
                                }
                            }
                        }
                    }]
                };
                option && myChart.setOption(option);                
            })


        },    
    },
};
</script>

<style scoped>
.bottom {
    margin-bottom: 0 !important;
    height: 117px;
}
.rightpart {
    margin-top: 0px;
    height: 463.6px;
}
</style>