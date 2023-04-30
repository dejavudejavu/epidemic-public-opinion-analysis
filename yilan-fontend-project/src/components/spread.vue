<template>
    <div class="c-mains c-m-box" style="top: 112px">
        <div class="c-m-flex-2 c-m-flex;" style="margin-right: 30px">
            <c-box style="width: 100%; height: 100%">
                <template v-slot:main >
                <div  style='display: flex;height: 100%; flex-direction: column;'>
                    <div class="c-list-head headtext" style="padding-left: 0">
                        <div style="text-align: center"   class="c-l-title"><span>传播途径</span></div>
                    </div>
                    <div
                        class="c-list-text t-over"
                        style="height: 100%"
                        id="chart1"
                    ></div>                
                </div>

                </template>
            </c-box>
        </div>
        <div class="c-m-flex-1 c-m-flex" style='display:flex;flex-direction:column'>
            <c-box style="width: 100%; height: 35.66%;flex:1">
                <template v-slot:main>
                    <div class="c-list-head headtext" style="padding-left: 0;flex:1">
                        <img
                            src="../../public/images/chartbg_head.png"
                            style="float: left; margin-top: 2px"
                        />
                        <div style="text-align: center;text-indent:0"   class="color-title">热点新闻</div>
                    </div>
                    <div  class="full-box">
                        <div style='display: flex;flex-direction: column;height: 100%;'>
                            <div v-for="(item,index) in news" :key="index" class="c-list-item" style="display:flex;flex:1" @click='handleClick(index)'  @mouseover="hover = index"  @mouseleave="hover = -1" :class="{'hoverStyle':hover==index&&clk!=index,'clkStyle':clk==index} ">                        
                                <div class="c-list-text t-over listItem" style ='flex:1'>
                                    <el-avatar size="38" :src="item.avatar" style='position: relative;top: 50%;transform: translate(0, -50%);'></el-avatar>
                                </div>                                
                                <div class="c-list-text t-over listItem" style ='flex:10;color:white'>
                                        <span class='t-over' style='position: absolute; top: 50%;transform: translate(0, -50%);width:100%'>{{ item.content }}  </span>                                 
                                </div>
                                <div class="c-list-text t-over listItem" style ='flex:1.5;' >
                                    <a
                                        :href="item.url"
                                        style="color: aquamarine;position: absolute; top: 50%;transform: translate(0, -50%);"
                                    >详情>></a>    
                                </div>                                   
                    
                            </div>
                        </div>                    
                    </div>
                </template>
            </c-box>
            <c-box style="width: 100%; height: 30%; margin-top: 3.33%;flex:1">
                <template v-slot:main>
                    <div class="c-list-head headtext" style="padding-left: 0">
                        <img
                            src="../../public/images/chartbg_head.png"
                            style="float: left; margin-top: 2px"
                        />                        
                        <div style="text-align: center;text-indent:0"   class="color-title">转发热度</div>
                    </div>
                    <div id="chart2" class="full-box"></div>
                </template>
            </c-box>
            <c-box style="width: 100%; height: 30%; margin-top: 3.33%;flex:1">
                <template v-slot:main>
                    <div class="c-list-head headtext" style="padding-left: 0">
                        <img
                            src="../../public/images/chartbg_head.png"
                            style="float: left; margin-top: 2px"
                        />                        
                        <div style="text-align: center;text-indent:0"   class="color-title">层级分析</div>
                    </div>
                    <div id="chart3" class="full-box"></div>
                </template>
            </c-box>
        </div> 
    </div>
</template>

<script>
// import $ from "jquery";
export default {
    data() {
        return {
            myChartz:null,
            myChartg:null,
            myChartb:null,         
            clk:0,
            hover:-1,
            hoverStyle:'hoverStyle',
            clkStyle:'clkStyle',
            isUpdateList: true,
            leftState: 1,
            news:[],
            listHead: [
                {
                    name: "传播途径",
                },
                {
                    name: "层级分析",
                },
            ],
            itemsData: [
                {
                    comment: "WIFI致癌",
                    date: "2020年1月1日",
                    reliability: "1%",
                    result: "假",
                    resource: "新浪微博",
                },
            ],
        };
    },
    mounted() {
        this.getNews();        
        this.zhuanfa(0);
        this.bili(0);
        this.guanxi(0);
    },
    beforeDestroy () { 
         this.myChartz.clear()   
         this.myChartg.clear()   
         this.myChartb.clear()          
    },      
    methods: {
        handleClick(index) {
            this.clk=index
            this.guanxi(index);
            this.bili(index);
            this.zhuanfa(index);
        },
        scrollYEvent() {},
        //转发次数和时间折线图
        zhuanfa(index) {
            this.myChartz = this.$echarts.init(document.getElementById("chart2"))
            this.axios.get(this.baseUrl+'/yilan-json/spread/repostSum.json').then((res)=>{
                var data=res.data[index]
                
                var option = {
                    backgroundColor: 'rgba(1,42,53,0.8)',                    
                    textStyle:{
                        fontSize:16,
                        color:'white'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: data.Date,                        
                    },
                    yAxis: {
                        type: 'value',
                        axisLabel: {
                            formatter: '{value} 次'
                        }
                    },
                    grid:{
                        top:50,
                        bottom:20,
                        right:55
                    },
                    series: [
                        {
                            name: '转发次数',
                            type: 'line',
                            data: data.data,
                            markPoint: {
                                data: [
                                    {type: 'max', name: '最大值'},
                                    {type: 'min', name: '最小值'}
                                ]
                            },
                            markLine: {
                                data: [
                                    {type: 'average', name: '平均值'}
                                ]
                            }
                        },
                    ]
                }; 
                option && this.myChartz.setOption(option);                               
            })
        },
        //转发关系图
        guanxi(index) {
            var chartDom = document.getElementById("chart1");
            this.myChartg = this.$echarts.init(chartDom);
            var option;
            this.myChartg.showLoading();
            this.axios.get(this.baseUrl+'/yilan-json/spread/newsSpread'+index+'.json').then((res)=>{
                    this.myChartg.hideLoading();
                    var links=res.data.links
                    var nodes=res.data.nodes
                    var sourceItem={
                        id:index+'',
                        name:this.news[index].content,
                        url:this.news[index].url,
                        category:0,
                        symbolSize:'70',
                        // itemStyle:{
                        //     color:'#C74F77'
                        // }
                    }
                    nodes.push(sourceItem);                       
                    var categories= [
                    {
                        "name": "首发"
                    },
                    {
                        "name": "第一层"
                    },
                    {
                        "name": "第二层"
                    },
                    {
                        "name": "第三层"
                    },
                    {
                        "name": "第四层"
                    },
                    {
                        "name": "第五层"
                    },
                    {
                        "name": "第六层"
                    }
                    ]              
                    option = { 
                        tooltip: {},
                        color: ['#C74F77','#E5EFC1','#42A5F5','#26C6DA','#5FEDD5','#91F2FF','#FFFFFF'],
                        legend: [{
                            // selectedMode: 'single',
                            backgroundColor: '#020f18',
                            data: categories.map(function (a) {
                                return a.name;
                            }),
                            textStyle:{
                                fontSize:20,
                                color:'white'
                            },                              
                        }],
                        series: [
                            {
                                textStyle:{
                                    fontSize:16,
                                    color:'white'
                                },                                  
                                type: "graph",
                                layout: "force",
                                data: nodes,
                                links:links,
                                draggable: true,
                                zoom:0.8,
                                categories: categories,
                                roam: true,
                                label: {
                                    show: true,
                                    position: "right",
                                    formatter: "{b}",
                                },
                                labelLayout: {
                                    hideOverlap: true,
                                },
                                scaleLimit: {
                                    min: 0.01,
                                    max: 5,
                                },
                                lineStyle: {
                                    color:" white",
                                    curveness: 0.3,
                                },
                            },
                        ],
                    };
                    this.myChartg.setOption(option);             
                
            }).catch((err)=>{
                
            })
            option && this.myChartg.setOption(option);
            this.myChartg.on('click', (params)=>{
                
                var data=params.data
                if(data.url!=undefined){
                     window.open(params.data.url) 
                }
            })
        },
        //比例饼图
        bili(index) {
            var chartDom = document.getElementById("chart3");
            this.myChartb = this.$echarts.init(chartDom);
            var option;
            this.axios.get(this.baseUrl+'/yilan-json/spread/level.json').then((res)=>{                
            var data = res.data[index];
            
            var names=['','第一层','第二层','第三层','第四层','第五层','第六层',]
            var value=[]
            for(var i=1;i<=6;i++){
                var item={
                    value:data[i],
                    name:names[i]
                }
                value.push(item)
            }            
            option = {
                backgroundColor: 'rgba(1,42,53,0.8)',                                    
                legend: {
                    orient:'vertical',
                    right:'right',
                    top:'middle',
                    textStyle: {
                        color: 'white'
                    }                    
                },
                tooltip: {
                    trigger: 'item'
                },                
                series: [
                    {
                        name: '转发层级',
                        type: 'pie',
                        radius: [10, 100],
                        center: ['50%', '50%'],
                        roseType: 'area',
                        itemStyle: {
                            borderRadius: 8
                        },
                        data: value
                    }
                ]
            };       
            option && this.myChartb.setOption(option);                     
            })


        },
        //获取热点新闻
        getNews(){
            this.axios.get(this.baseUrl+'/yilan-json/spread/hotNews.json').then((res)=>{
                this.news=res.data
            })
        }
    },
};
</script>

<style scoped>
.headtext {
    color: white;
}
.bottom {
    margin-bottom: 0 !important;
    height: 117px;
}
.hoverStyle{
    background:darkgray;
}
.clkStyle{
    background:darkseagreen;
}
</style>
