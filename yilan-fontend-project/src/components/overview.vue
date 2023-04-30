<template>
    <div class="c-mains" style='display: flex; flex-direction: column;'>
        <!-- 第一层 -->
        <div class="c-m-box" style="height: 300px;flex:2">            
            <!-- 左上 -->
            <div class="c-m-flex-3 c-m-flex">
                <div id='china' style='height: 550px;'></div>
            </div>
            <!-- 右上 -->
            <div class="c-m-flex-2 c-m-flex" style="padding-left: 30px">
                <c-box class="c-r-box c-r-box1" style="height:266px">
                    <template v-slot:main>
                        <img
                            src="../../public/images/chartbg_head.png"
                            style="float: left; margin-top: 2px"
                        />
                        <div class="c-r-title">疫情概述</div>
                        <div style="font-size: 19px;color: white;letter-spacing: 1px;   line-height: 2;   padding: 23px 10px;background: rgba(1,42,53,0.8)">
                            {{ content }}
                            <a
                                href="http://www.nhc.gov.cn/xcs/yqfkdt/gzbd_index.shtml"
                                style="color: aquamarine"
                                >最新情况>></a
                            >
                        </div>
                    </template>
                </c-box>                
                <div style='height:25%'>
                    <div class='shuoming' style='padding-top:20px;display:inline-block;width:20%;height:100%;vertical-align: bottom;color:#545a65;line-height: 1.5;'>
                        <div>
                            <i class='el-icon-info'></i>
                            说明：<br>
                            真实值:真实言论占比<br>
                            情感值:积极情感占比
                        </div>                        
                    </div>                    
                    <div class="yibiao" id='yibiao1'>

                    </div>
                    <div class="yibiao" id='yibiao2'>

                    </div>

                </div>
            </div>
        </div>
        <div class="c-m-box c-m-box-item" style="top:520px; bottom: 0;flex:1">
            <!-- 左下 -->
            <div class="c-m-flex-3 c-m-flex">
                <div  class="c-r-main"  >
                    <div class="tab-head">
                        <div class="cur long tab-btn2-active">疫情大事记</div>
                    </div>
                    <c-box class="tab-main">
                        <template v-slot:main>
                            <!-- 谣言分析 -->
                            <div style="height:100%">
                                <div style="height: 70%; width: 40%;position: relative;left: 4%; top:8%;overflow:hidden;z-index:20">
                                    <img :src="preImage" alt="" style="height：100%;width:100%;object-fit:cover;overflow:hidden"/>
                                </div>                                
                                <div id="shijianzhou" class="pie-items" style='z-index:10'>
                                </div>
                            </div>
                        </template>
                    </c-box>
                </div>
            </div>
            <!-- 右下 -->
            <div class="c-m-flex-2 c-m-flex" style="margin-left: 30px">
                <div class="c-r-main" id="windowAttack">
                    <div class="tab-head">
                        <div class="tab-btn1-active cur">热度趋势</div>
                    </div>
                    <c-box class="tab-main">
                        <template v-slot:main>
                            <!--舆情情感 -->
                            <div class="">
                                <div id="pies" class="pie-items" style='' ></div>
                            </div>
                        </template>
                    </c-box>
                </div>                
            </div>
        </div>
        <!-- 下侧 -->
        <!-- 中间 -->
    </div>
</template>

<script scoped>
// import $ from 'jquery'
// import word from "../../public/images/word.png"
export default {
    data() {
        return {
            myChart:null,
           myCharte:null,
           myChartc:null,
           myChartl:null,
           myCharth:null,
            texts: {
                title: "新冠",
            },
            preImage:'',
            images: [
                'http://159.75.23.139:3000/test/1.png',
                'http://159.75.23.139:3000/test/2.png',   
                'http://159.75.23.139:3000/test/3.png',
                'http://159.75.23.139:3000/test/4.jpg',  
                'http://159.75.23.139:3000/test/5.png',
                'http://159.75.23.139:3000/test/6.jpg',   
                'http://159.75.23.139:3000/test/7.png',
                'http://159.75.23.139:3000/test/8.jpg', 
                'http://159.75.23.139:3000/test/9.jpg',                                                              
            ],
            // word,
            attackType: 1,
            eventTotals: [],
            deviceTotals: [],
            leftState: 1,
            leftData: [
                {
                    name: "曝光量",
                    value: 11180,
                    unit: "亿次",
                },
                {
                    name: "参与用户人数",
                    value: 22338,
                    unit: "人",
                },
            ],
            content:
                "常态化疫情防控，意味着我们进入“后疫情时期”。这一时期的特点是，疫情本土传播途径已经基本阻断，疫情得到有效控制，但疫情反弹风险依然存在。因此，疫情防控具有长期性、复杂性、艰巨性特点。社会重心将由集中打疫情防控阻击战转到一手抓疫情防控、一手抓经济社会发展。在今后较长一段时间，疫情防控将像影子一样跟随我们，融入到我们的工作生活学习中。”",
            saying:
                "“沉舟侧畔千帆过，病树前头万木春。”后疫情时代 的世界，必将如凤凰涅粲、焕发新生。让我们携手努力，共同创造更加美好幸福的生活，共同推动构建人类命运共同体!",
        };
    },
    beforeDestroy () {
         this.myChart.clear()        
         this.myCharte.clear()    
         this.myCharth.clear()   
         this.myChartc.clear()   
         this.myChartl.clear()          
    },    
    mounted() {
        this.heat(); 
        this.reality();
        this.emotion();  
        this.chinaMap();
        this.line()
    },
    methods: {
        line() {
            var chartDom = document.getElementById('shijianzhou');
            this.myChartl =  this.$echarts.init(chartDom);
            var option;   
            var img = new Image();
            img.src ='../assets/au.png'
            var timeLine=
        {
            "title":[
                "武汉新型冠状病毒肺炎新增136例",
                "北京确诊两例新型肺炎病例",
                "各地相继启动重大突发公共卫生事件",
                "全国确诊新型冠状病毒肺炎病例6078例",
                "“新冠肺炎”简称为“NCP”",
                "全球新冠肺炎确诊病例数超100万",
                "疫情已扩散至211个国家和地区",
                "全国31省区市全部解除一级响应",
                "5月1日新增确诊病例为1月16日以来最低",
                "全球累计新冠肺炎确诊病例超500万例",
                "中国4个新冠疫苗进入临床三期",
                "欧洲第二波疫情",
                "全球新冠确诊病例超5000万",
                "多国出现感染变异新冠病毒病例",
                "全球新冠确诊病例超8000万例",
                "中国新冠病毒疫苗上市",
                "河北:全省立即进入战时状态"
            ],
            "text":[
                "1月19日通报，1月18日0-24时，\n\n治愈出院5例，新增病例59例，死亡1例；\n\n1月19日0-22时，治愈出院1例，新增病例77例。",
                "1月20日凌晨，\n\n北京大兴区医疗机构接诊的两名有武汉旅行史的发热患者，\n\n经疾病预防控制中心检测及专家组评估，\n\n确认为新型冠状病毒感染的肺炎病例。\n\n两名患者已在定点医院接受隔离治疗，目前无呼吸道症状，病情平稳。",
                "在新冠肺炎疫情肆虐的情况下，\n\n结合各地新型冠状病毒感染的肺炎疫情防控形势，\n\n全国各省市相继启动重大突发公共卫生事件一级响应。",
                "截至1月29日18时，\n\n全国确诊新型冠状病毒肺炎病例6078例，\n\n其中115例出院，132例死亡。",
                "2月8日的国务院联防联控机制发布会上，\n\n卫健委发布关于新冠病毒感染的肺炎暂命名的通知，\n\n统一称谓为“新型冠状病毒肺炎”，简称“新冠肺炎”，\n\n英文名为“Novelcoronaviruspneumonia”，简称为“NCP”。",
                "全球新冠肺炎确诊病例超95万例，达951685例。\n\n此外，全球新冠肺炎死亡病例接近5万例，达48111例。\n\n中国以外新冠肺炎确诊病例升至744781例，\n\n死亡病例37456例。",
                "截至北京时间4月10日16时，\n\n疫情已扩散至全球211个国家和地区，\n\n累计确诊1568275例，\n\n“钻石公主”号邮轮712例，累计死亡92814例。",
                "5月1日，湖北省宣布，5月2日0时起，\n\n将湖北省突发公共卫生事件应急响应级别由一级调整至二级，\n\n并相应调整完善有关防控措施。\n\n至此，全国31个省区市均宣布解除一级响应。",
                "5月2日下午，国务院联防联控机制召开新闻发布会。\n\n，5月1日全国新增确诊病例1例，\n\n为1月16日以来最低。\n\n28个省份和新疆生产建设兵团已连续14天\n\n无新增本土确诊病例。",
                "截至北京时间5月20日16时18分左右，\n\n全球累计新冠肺炎确诊病例超500万例，达5000599例，\n\n累计死亡325156例。",
                "10月20日,科技部社会发展科技司副司长田保国当日表示，\n\n4个进入III期临床试验阶段的新冠疫苗，\n\n总体上进展顺利，截至到目前共计接种了约6万名受试者，\n\n未收到严重不良反应的报告。",
                "10月31日晚，英格兰地区自11月5日起开始实施第二次全面“封锁”，\n\n直至12月2日结束。\n\n同日，奥地利总理库尔茨宣布\n\n奥地利将从11月3日起再次实施全国“封锁”措施。",
                "截至美国东部时间11月8日11时24分（北京时间9日0时24分），\n\n全球累计新冠确诊病例超过5000万例，\n\n达50052204例，累计死亡病例1253110例。",
                "12月25日，多国宣布在本国境内出现感染变异新冠病毒的确诊病例。\n\n日本、黎巴嫩、爱尔兰先后宣布\n\n在本国境内出现感染变异新冠病毒的确诊病例。",
                "截至美国东部时间26日13时22分（北京时间27日2时22分），\n\n全球累计新冠确诊病例超过8000万例，\n\n达80081092例，累计死亡病例1753839例。\n\n从7000万例升至8000万例用时仅15天。",
                "12月31日，国务院联防联控机制发布，\n\n国药集团中国生物新冠灭活疫苗已获得国家药监局批准附条件上市。\n\n已有数据显示，保护率为79.34%，\n\n实现安全性、有效性、可及性、可负担性的统一，\n\n达到世界卫生组织及国家药监局相关标准要求。",
                "从1月2日报告首例病例至1月4日24时，\n\n河北省共报告本土确诊病例19例、无症状感染者40例。\n\n为严防疫情扩散，河北省立即启动应急机制，\n\n全面排查追踪，开展全员核酸检测，\n\n严格集中隔离场所规范管理，严格预检分诊和院感控制。",
            ],
            "date":[
                "2020-01-19",
                "2020-01-20",
                "2020-01-24",
                "2020-01-29",
                "2020-02-08",
                "2020-04-02",
                "2020-04-10",
                "2020-05-01",
                "2020-05-02",
                "2020-05-20",
                "2020-10-20",
                "2020-10-31",
                "2020-11-08",
                "2020-12-25",
                "2020-12-26",
                "2020-12-31",
                "2021-1-5"
            ]
        }    
            var years=timeLine.date
            var text=timeLine.text
            option = {
                baseOption: {
                    backgroundColor: 'rgba(1,42,53,0.8)',
                    timeline: {
                        bottom: '2%',
                        right: 50,
                        left:50,
                        axisType: 'category',
                        autoPlay: true,
                        playInterval: 1200,
                        label: {
                            normal: {
                                textStyle: {
                                    color: '#ddd'
                                }
                            },
                            emphasis: {
                                textStyle: {
                                    color: '#fff'
                                }
                            }
                        },
                        lineStyle: {
                            color: '#555'
                        },
                        checkpointStyle: {
                            color: '#bbb',
                            borderColor: '#777',
                            borderWidth: 2
                        },
                        controlStyle: {
                            showNextBtn: false,
                            showPrevBtn: false,
                            normal: {
                                color: '#666',
                                borderColor: '#666'
                            },
                            emphasis: {
                                color: '#aaa',
                                borderColor: '#aaa'
                            }
                        },
                        data: years
                    },

                    title: [{
                            text: '',
                            textAlign: 'center',
                            left: '70%',
                            // bottom: 80,
                            top: '8%',
                            // backgroundColor: 'rgba(1,42,53,0.8)',
                            borderRadius: 10,
                            triggerEvent:true,
                            padding: 18,
                            textStyle: {
                                fontSize: 20,
                                color: 'rgba(255, 255, 255, 0.9)'
                            }
                        },
                        {
                            text: '',
                            textAlign: 'center',
                            left: '70%',
                            // bottom: 80,
                            top: '20%',
                            // backgroundColor: 'rgba(1,42,53,0.8)',
                            borderRadius: 10,
                            triggerEvent:true,
                            padding: 18,
                            textStyle: {
                                fontSize: 20,
                                color: 'rgba(255, 255, 255, 0.9)'
                            }
                        }
                    ],
                    animationDurationUpdate: 2000,
                    animationEasingUpdate: 'quinticInOut'
                },
                options: []
            };
            for (var n = 0; n < years.length; n++) {
                option.options.push({
                    title: {
                        text: text[n]
                    },
                });
                
            } 
            option && this.myChartl.setOption(option); 

            this.myChartl.on('timelinechanged', (timeLineIndex)=>{
                var index=timeLineIndex.currentIndex
                this.preImage=this.baseUrl+'/newsImage/'+index+'.jpg'
             });             
        },
        chinaMap(){
            var chartDom = document.getElementById('china');
            this.myChartc =  this.$echarts.init(chartDom);
            var name_title = "各省在疫情相关话题被提及次数"
            var subname = '数据爬取自微博、知乎、今日头条'
            var nameColor = " rgb(55, 75, 113)"
            var name_fontFamily = '等线'
            var subname_fontSize = 15
            var name_fontSize = 18
            var mapName = 'china'
            this.axios.get(this.baseUrl+'/yilan-json/overview/area.json').then((res)=>{
                var data=res.data.data
                var geoJson=res.data.map
                var geoCoordMap = {};

                /*获取地图数据*/
                // this.this.myChart.showLoading();

                this.$echarts.registerMap('china', geoJson);
                // )
                // var mapFeatures = this.$echarts.getMap(mapName).geoJson.features;
                // this.this.myChart.hideLoading();
                geoJson.features.forEach(function(v) {
                    // 地区名称
                    var name = v.properties.name;
                    // 地区经纬度
                    geoCoordMap[name] = v.properties.cp;

                });

                
                var max = 500,
                    min = 10; // todo 
                var maxSize4Pin = 50,
                    minSize4Pin = 20;

                var convertData = function(data) {
                    var res = [];
                    for (var i = 0; i < data.length; i++) {
                        var geoCoord = geoCoordMap[data[i].name];
                        if (geoCoord) {
                            res.push({
                                name: data[i].name,
                                value: geoCoord.concat(data[i].value),
                            });
                        }
                    }
                    
                    return res;
                };
                var option = {
                    title: {
                        text: name_title,
                        subtext: subname,
                        x: 'center',
                        textStyle: {
                            color: nameColor,
                            fontFamily: name_fontFamily,
                            fontSize: name_fontSize,                        
                        },
                        subtextStyle:{
                            fontSize:subname_fontSize,
                            fontFamily:name_fontFamily
                        }
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: function(params) {
                            
                            if(params.data.scale){
                                var toolTiphtml = params.data.name+':<br>'+params.data.scale
                                return toolTiphtml;
                            }
                            return;
                        },
                        axisPointer: {
                            type: 'shadow'
                        },                    
                    },
                    visualMap: {
                        textStyle: {
                            color: "white",                    
                        },                    
                        show: true,
                        min: 0,
                        max:1000,
                        left: 'left',
                        bottom: '10%',
                        text: ['高', '低'], // 文本，默认为数值文本
                        calculable: true,
                        seriesIndex: [1],
                        inRange: {
                            // color: ['#3B5077', '#031525'] // 蓝黑
                            // color: ['#ffc0cb', '#800080'] // 红紫
                            // color: ['#3C3B3F', '#605C3C'] // 黑绿
                            // color: ['#0f0c29', '#302b63', '#24243e'] // 黑紫黑
                            // color: ['#23074d', '#cc5333'] // 紫红
                            // color: ['#00467F', '#A5CC82'] // 蓝绿
                            // color: ['#1488CC', '#2B32B2'] // 浅蓝
                            color: ['#24CFF4', '#2E98CA','#1E62AC'] // 蓝绿
                            // color: ['#00467F', '#A5CC82'] // 蓝绿
                            // color: ['#00467F', '#A5CC82'] // 蓝绿
                            // color: ['#00467F', '#A5CC82'] // 蓝绿

                        }
                    },
                    geo: {
                        show: true,
                        map: mapName,
                        zoom: 1.2,
                        label: {
                            normal: {
                                show: true,
                                color: "rgb(249, 249, 249)",
                            },
                            emphasis: {
                                show: true,
                                color: '#f75a00',                        
                            }
                        },
                        roam: true,
                        itemStyle: {
                            normal: {
                                areaColor: '#24CFF4',
                                borderColor: '#53D9FF',
                                borderWidth: 1.3,
                                shadowBlur: 15,
                                shadowColor: 'rgb(58,115,192)',
                                shadowOffsetX: 7,
                                shadowOffsetY: 6,
                            },
                            emphasis: {
                                areaColor: '#8dd7fc',
                                borderWidth: 1.6,
                                shadowBlur: 25,
                            }
                        }
                    },
                series: [{
                        name: '散点',
                        type: 'scatter',
                        coordinateSystem: 'geo',
                        data: convertData(data),
                        symbolSize: function(val) {
                            return val[2] / 10;
                        },
                        label: {
                            // normal: {
                            //     formatter: '{b}',
                            //     position: 'right',
                            //     show: true
                            // },
                            // emphasis: {
                            //     show: true
                            // }
                        },
                        itemStyle: {
                            normal: {
                                color: '#05C3F9'
                            }
                        }
                    },
                    {
                        type: 'map',
                        map: mapName,
                        geoIndex: 0,
                        zoom: 2,
                        aspectScale: 0.75, //长宽比
                        showLegendSymbol: false, // 存在legend时显示
                        label: {
                            // normal: {
                            //     show: true
                            // },
                            // emphasis: {
                            //     show: false,
                            //     textStyle: {
                            //         color: '#fff'
                            //     }
                            // }
                        },
                        roam: true,
                        itemStyle: {
                            normal: {
                                areaColor: '#031525',
                                borderColor: '#3B5077',
                            },
                            emphasis: {
                                areaColor: '#2B91B7'
                            }
                        },
                        animation: false,
                        data: data
                    },
                    {
                        name: '点',
                        type: 'scatter',
                        coordinateSystem: 'geo',
                        symbol: 'pin', //气泡                    
                        symbolSize: function(val) {
                            var a = (maxSize4Pin - minSize4Pin) / (max - min);
                            var b = minSize4Pin - a * min;
                            b = maxSize4Pin - a * max;
                            return a * val[2] + b;
                        },
                        label: {
                            normal: {
                                formatter: '{@[2]}',
                                show: true,
                                textStyle: {
                                    color: '#fff',
                                    fontSize: 9,
                                }
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#F62157', //标志颜色
                            }
                        },
                        zlevel: 6,
                        data: convertData(data),
                    },
                    {
                        name: 'Top 5',
                        type: 'effectScatter',
                        coordinateSystem: 'geo',
                        data: convertData(data.sort(function(a, b) {
                            return b.value - a.value;
                        }).slice(0, 5)),
                        symbolSize: function(val) {
                            return val[2] / 25;
                        },
                        showEffectOn: 'render',
                        rippleEffect: {
                            brushType: 'stroke'
                        },
                        hoverAnimation: true,
                        label: {
                            // normal: {
                            //     formatter: '{b}',
                            //     position: 'right',
                            //     show: true
                            // }
                        },
                        itemStyle: {
                            normal: {
                                color: 'yellow',
                                shadowBlur: 10,
                                shadowColor: 'yellow'
                            }
                        },
                        zlevel: 1
                    },

                ]
                };
                this.myChartc.setOption(option);                                
            })            
                
          
        },  
        reality(){
            var chartDom = document.getElementById('yibiao1');
           this.myChart =  this.$echarts.init(chartDom);
            let value = 39.83;
            let title = '真实值';
            let int = value.toFixed(2).split('.')[0];
            let float = value.toFixed(2).split('.')[1];
            var option = {
                // backgroundColor: '#020f18',
                title: {
                    text: '{a|' + int + '}{b|.' + float +'%'+ '}\n{c|' + title + '}',
                    x: 'center',
                    y: 'center',
                    textStyle: {
                        rich: {
                            a: {
                                fontSize: 48,
                                color: '#fff',
                                fontWeight:'600',
                            },
                            b: {
                                fontSize: 20,
                                color: '#fff',
                                padding: [0, 0, 14, 0]
                            },
                            c: {
                                fontSize: 20,
                                color: '#fff',
                                padding: [5, 0]
                            }
                        }
                    }
                },
                series: [
                    {
                        type: 'gauge',
                        radius: '90%',
                        clockwise: false,
                        startAngle: '90',
                        endAngle: '-269.9999',
                        splitNumber: 30,
                        detail: {
                            offsetCenter: [0, -20],
                            formatter: ' '
                        },
                        pointer: {
                            show: false
                        },
                        axisLine: {
                            show: true,
                            lineStyle: {
                                color: [
                                    [0, '#2CFAFC'],
                                    [60.17 / 100, '#0ff'],
                                    [1, '#0f232e']
                                ],
                                width: 20
                            }
                        },
                        axisTick: {
                            show: false
                        },
                        splitLine: {
                            show: true,
                            length: 100,
                            lineStyle: {
                                shadowBlur: 10,
                                shadowColor: 'rgba(0, 255, 255, 1)',
                                shadowOffsetY:'0',
                                color: '#020f18',
                                width: 2
                            }
                        },
                        axisLabel: {
                            show: false
                        }
                    },
                    {
                        type: 'pie',
                        radius: ['64%', '66%'],
                        hoverAnimation: false,
                        clockWise: false,
                        itemStyle: {
                            normal: {
                                color: '#0C355E'
                            }
                        },
                        label: {
                            show: false
                        },
                        data: _dashed()
                    },
                    
                    {
                        type: 'pie',
                        radius: [0, '50%'],
                        hoverAnimation: false,
                        clockWise: false,
                        itemStyle: {
                            normal: {
                                shadowBlur: 20,
                                shadowColor: '#000',
                                color: new this.$echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                                    offset: 0,
                                    color: '#0FF',
                                }, {
                                    offset: 1,
                                    color: '#060f20'
                                }])
                            }
                        },
                        label: {
                            show: false
                        },
                        data: [100]
                    },
                    {
                        type: 'pie',
                        radius: ['64%', '65.5%'],
                        hoverAnimation: false,
                        clockWise: false,
                        itemStyle: {
                            normal: {
                                shadowBlur: 20,
                                shadowColor: 'rgba(0, 255, 255,.3)',
                                color: '#0f232e'
                            }
                        },
                        label: {
                            show: false
                        },
                        data: [100]
                    },
                    {
                        type: 'pie',
                        radius: ['68%', '69.5%'],
                        hoverAnimation: false,
                        clockWise: false,
                        itemStyle: {
                            normal: { 
                                shadowBlur: 20,
                                shadowColor: 'rgba(0, 255, 255,.3)',
                                color: 'rgba(15, 35, 46,.6)',
                            }
                        },
                        label: {
                            show: false
                        },
                        data: [100]
                    },
                ]
            };

            function _dashed() {
                let dataArr = [];
                for (var i = 0; i < 100; i++) {
                    if (i % 2 === 0) {
                        dataArr.push({
                            name: (i + 1).toString(),
                            value: 20,
                            itemStyle: {
                                normal: {
                                    color: 'rgb(0,255,255,.3)',
                                }
                            }
                        })
                    } else {
                        dataArr.push({
                            name: (i + 1).toString(),
                            value: 20,
                            itemStyle: {
                                normal: {
                                    color: 'rgb(0,0,0,0)',
                                    borderWidth: 1,
                                    borderColor: "rgba(0,255,255,1)"
                                }
                            }
                        })
                    }

                }
                return dataArr

            }

            function doing() {
                let option =this.myChart.getOption();
                option.series[1].startAngle = option.series[1].startAngle - 1;
               this.myChart.setOption(option);
            }
            function startTimer() {
                setInterval(doing, 100);
            }
            setTimeout(startTimer, 0);

            option && this.myChart.setOption(option);
        },
        emotion(){
            var chartDom = document.getElementById('yibiao2');
           this.myCharte =  this.$echarts.init(chartDom);
            let value = 15.67;
            let title = '情感值';
            let int = value.toFixed(2).split('.')[0];
            let float = value.toFixed(2).split('.')[1];
            var option = {
                // backgroundColor: '#020f18',
                title: {
                    text: '{a|' + int + '}{b|.' + float +'%'+ '}\n{c|' + title + '}',
                    x: 'center',
                    y: 'center',
                    textStyle: {
                        rich: {
                            a: {
                                fontSize: 48,
                                color: '#fff',
                                fontWeight:'600',
                            },
                            b: {
                                fontSize: 20,
                                color: '#fff',
                                padding: [0, 0, 14, 0]
                            },
                            c: {
                                fontSize: 20,
                                color: '#fff',
                                padding: [5, 0]
                            }
                        }
                    }
                },
                series: [
                    {
                        type: 'gauge',
                        radius: '90%',
                        clockwise: false,
                        startAngle: '90',
                        endAngle: '-269.9999',
                        splitNumber: 30,
                        detail: {
                            offsetCenter: [0, -20],
                            formatter: ' '
                        },
                        pointer: {
                            show: false
                        },
                        axisLine: {
                            show: true,
                            lineStyle: {
                                color: [
                                    [0, '#2CFAFC'],
                                    [84.33/ 100, '#e24a83'],
                                    [1, '#0f232e']
                                ],
                                width: 20
                            }
                        },
                        axisTick: {
                            show: false
                        },
                        splitLine: {
                            show: true,
                            length: 100,
                            lineStyle: {
                                shadowBlur: 10,
                                shadowColor: 'rgba(0, 255, 255, 1)',
                                shadowOffsetY:'0',
                                color: '#e24a83',
                                width: 2
                            }
                        },
                        axisLabel: {
                            show: false
                        }
                    },
                    {
                        type: 'pie',
                        radius: ['64%', '66%'],
                        hoverAnimation: false,
                        clockWise: false,
                        itemStyle: {
                            normal: {
                                color: '#0C355E'
                            }
                        },
                        label: {
                            show: false
                        },
                        data: _dashed()
                    },
                    
                    {
                        type: 'pie',
                        radius: [0, '50%'],
                        hoverAnimation: false,
                        clockWise: false,
                        itemStyle: {
                            normal: {
                                shadowBlur: 20,
                                shadowColor: '#000',
                                color: new this.$echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                                    offset: 0,
                                    color: '#e28c6f',
                                }, {
                                    offset: 1,
                                    color: '#e24a83'
                                }])
                            }
                        },
                        label: {
                            show: false
                        },
                        data: [100]
                    },
                    {
                        type: 'pie',
                        radius: ['64%', '65.5%'],
                        hoverAnimation: false,
                        clockWise: false,
                        itemStyle: {
                            normal: {
                                shadowBlur: 20,
                                shadowColor: 'rgba(0, 255, 255,.3)',
                                color: '#0f232e'
                            }
                        },
                        label: {
                            show: false
                        },
                        data: [100]
                    },
                    {
                        type: 'pie',
                        radius: ['68%', '69.5%'],
                        hoverAnimation: false,
                        clockWise: false,
                        itemStyle: {
                            normal: { 
                                shadowBlur: 20,
                                shadowColor: 'rgba(0, 255, 255,.3)',
                                color: 'rgba(15, 35, 46,.6)',
                            }
                        },
                        label: {
                            show: false
                        },
                        data: [100]
                    },
                ]
            };

            function _dashed() {
                let dataArr = [];
                for (var i = 0; i < 100; i++) {
                    if (i % 2 === 0) {
                        dataArr.push({
                            name: (i + 1).toString(),
                            value: 20,
                            itemStyle: {
                                normal: {
                                    color: '#e24a83',
                                }
                            }
                        })
                    } else {
                        dataArr.push({
                            name: (i + 1).toString(),
                            value: 20,
                            itemStyle: {
                                normal: {
                                    color: 'rgb(0,0,0,0)',
                                    borderWidth: 1,
                                    borderColor: "#e28c6f"
                                }
                            }
                        })
                    }

                }
                return dataArr

            }

            function doing() {
                let option = this.myCharte.getOption();
                option.series[1].startAngle = option.series[1].startAngle - 1;
                this.myCharte.setOption(option);
            }
            function startTimer() {
                setInterval(doing, 100);
            }
            setTimeout(startTimer, 0);

            option && this.myCharte.setOption(option);
        },
        heat() {
            this.myCharth = this.$echarts.init(document.getElementById("pies"));
            var xData = function() {
                var data = [];
                for (var i = 1; i < 31; i++) {
                    data.push(i + "日");
                }
                return data;
            }();
            this.axios.get(this.baseUrl+'/yilan-json/overview/heat.json').then((res)=>{
                var zhihu=res.data.items[0];
                var weibo=res.data.items[1];
                var toutiao=res.data.items[2];
                var zongti=res.data.items[3];
                var date=res.data.date
                var option = {
                    backgroundColor:  'rgba(1,42,53,0.8)',
                    tooltip: {
                        trigger: "axis",
                        axisPointer: {
                            type: "shadow",
                            textStyle: {
                                color: "#6ce8b6"
                            }
                        },
                    },
                    grid: {
                        borderWidth: 0,
                        top: 50,
                        bottom: 60,
                        textStyle: {
                            color: "#6ce8b6"
                        }
                    },
                    legend: {
                        x: '46%',
                        top: '1%',
                        textStyle: {
                            color: '#26b2e8',
                        },
                        data: ['知乎', '微博',"头条","总体"]
                    },
                    calculable: true,
                    xAxis: [{                    
                        type: "category",
                        axisLine: {
                            lineStyle: {
                                color: "#26b2e8",
                            }
                        },
                        splitLine: {
                            show: false
                        },
                        axisTick: {
                            show: false
                        },
                        data: date,
                    }],
                    yAxis: [{
                        type: "value",
                        splitLine: {
                            show: false
                        },
                        axisLine: {
                            lineStyle: {
                                color: "#26b2e8",
                            }
                        },

                    }],
                    dataZoom: [{
                        show: true,
                        height: '5%',
                        xAxisIndex: [0],
                        bottom: '4%',
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
                        fillerColor:"rgba(67,55,160,0.4)",
                        borderColor: "rgba(204,187,225,0.5)",

                    }, 
                    {
                        type: "inside",
                        show: true,
                        height: 15,
                        start: 1,
                        end: 35
                    }],
                    series: [
                        {
                        name: zhihu.title,
                        type: "line",
                        symbolSize: 10,
                        symbol: 'circle',
                        itemStyle: {
                            color: "#6f7de3",
                        },
                        markPoint: {
                            label: {
                                normal: {
                                    textStyle: {
                                        color: '#fff'
                                    }
                                }
                            },
                            data: [{
                                type: 'max',
                                name: '最大值',

                            }, {
                                type: 'min',
                                name: '最小值'
                            }]
                        },
                        data: zhihu.data,
                    }, 
                    {
                        name: weibo.title,
                        type: "line",
                        symbolSize: 10,
                        symbol: 'circle',
                        itemStyle: {
                            color: "#c257F6",
                        },
                        markPoint: {
                            label: {
                                normal: {
                                    textStyle: {
                                        color: '#fff'
                                    }
                                }
                            },
                            data: [{
                                type: 'max',
                                name: '最大值',

                            }, {
                                type: 'min',
                                name: '最小值'
                            }]
                        },
                        data: weibo.data
                    }, 
                    {
                        name: toutiao.title,
                        type: "line",
                        symbolSize: 10,
                        symbol: 'circle',
                        itemStyle: {
                            color: "#2c9a42",
                        },
                        markPoint: {
                            label: {
                                normal: {
                                    textStyle: {
                                        color: '#fff'
                                    }
                                }
                            },
                            data: [{
                                type: 'max',
                                name: '最大值',

                            }, {
                                type: 'min',
                                name: '最小值'
                            }]
                        },
                        data:toutiao.data
                    },  
                    {
                        name: zongti.title,
                        type: "line",
                        symbolSize: 10,
                        symbol: 'circle',
                        itemStyle: {
                            color: "#c23c33",
                        },
                        markPoint: {
                            label: {
                                normal: {
                                    textStyle: {
                                        color: '#fff'
                                    }
                                }
                            },
                            data: [{
                                type: 'max',
                                name: '最大值',

                            }, {
                                type: 'min',
                                name: '最小值'
                            }]
                        },
                        data:zongti.data
                    },                                         
                    ]
                }
                option && this.myCharth.setOption(option);                
            })


        },
    },
};
</script>

<style scoped>
.long{
    width:166px
}
.yibiao{
    display: inline-block;
    height: 100%;
    width: 40%;
}
.bottom {
    margin-bottom: 22.1px !important;
    height: 214px;
}
</style>