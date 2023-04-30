<template>
    <div class="c-mains" style="top: 142px;">
        <!-- bottom list -->
        <div style='display:flex;height:100%'>
            <div id='tupu' style='flex:1;top:-45px;position:relative;height:120%'></div>
            <div class="effect-list">
                <div class="list-title" style="top: -57px">热帖排行榜</div>
                <div class="c-main-top" style="transform: none;left: auto; right: 20px;top: -41px;">
                    <div class="" >
                        <div class="c-main-t">选择平台</div>
                        <div class="c-select text-over" @click="listShow = true">{{platform}}</div>
                        <c-scroll class="c-select-items" style="height:71px" v-show="listShow">
                            <template v-slot:main>
                                <div class="c-select-item" v-for="item in platforms" :key="item.name"
                                    @click="handleClick(item)">{{item.name}}</div>
                            </template>
                        </c-scroll>
                    </div>
                </div>            
                <div class="c-list" style="top: -51px;height:100%" v-loading="loading">
                    <!-- head -->
                    <c-box style="width: 100%">
                        <template v-slot:main>
                            <div class="c-list-head">
                                <div
                                    v-for="(item, index) in listHead"
                                    ::key="item.name"
                                    :style="item.style"
                                    :key="index"
                                    style="color: white;text-align: center"
                                >
                                <i :class="item.icon"></i>
                                    {{ item.name }}
                                </div>
                            </div>
                        </template>
                    </c-box>
                    <c-scroll
                        class="c-list-main"
                        ref="list" 
                    >
                        <template v-slot:main>
                            <div>
                                <div
                                    v-for="item in itemsData"
                                    :key="item.id"
                                    class="c-list-item"
                                    style="height: 45px"
                                >
                                    <img src="../assets/au.png" v-if='item.rank==1' class='medal'/>
                                    <img src="../assets/silver.png" v-else-if='item.rank==2' class='medal'/>
                                    <img src="../assets/cu.png" v-else-if='item.rank==3' class='medal'/>                            
                                    <div class="c-list-text t-over" :style="listHead[0].style">
                                        <div class="num-font c-l-num">
                                            {{ item.rank }}
                                        </div> 
                                    </div>                                                              
                                    <div class="c-list-text t-over" :style="listHead[1].style" >   
                                        <div v-if="item.content!=''"  class="c-list-text t-over">
                                            <el-link :href="item.url" target="_blank" class="c-list-text t-over" >{{ item.content }}</el-link>
                                        </div>
                                        <div v-else>
                                            <i class="el-icon-warning"></i>
                                            <el-link :href="item.url" target="_blank">内容为视频</el-link>
                                        </div>
                                    </div>
                                    <div class="c-list-text t-over" :style="listHead[2].style" >
                                        {{ item.upper }}
                                    </div>
                                    <div class="c-list-text t-over" :style="listHead[3].style">
                                        {{ item.comment }}
                                    </div>
                                    <div class="c-list-text t-over" :style="listHead[4].style">
                                        {{ item.thumbUp }}
                                    </div>
                                    <div class="c-list-text t-over" :style="listHead[5].style">
                                        <div v-if='item.rePost'>
                                            {{ item.rePost}}                                        
                                        </div>
                                        <div v-else>
                                            暂无数据
                                        </div>
                                    </div>                                
                                </div>
                            </div>
                        </template>
                    </c-scroll>
                </div>
            </div>            
        </div>

    </div>
</template>

<script>
export default {
    data() {
        return {
            myChart:null,
            loading: false,
            platform:'知乎',
            listShow:false,
            platforms:[
                {
                    name:'知乎',
                    id:'zhihu',
                    index:0
                },
                {
                    name:'微博',
                    id:'weibo',
                    index:1
                },

                {
                    name:'今日头条',
                    id:'toutiao',
                    index:2
                }
            ],
            dayVal:10,
            days:[1,2,3,4,5,6,7,8,9],
            texts: {
                title: "今日头条",
            },
            attackType: 1,
            eventTotals: [],
            deviceTotals: [],
            leftState: 1,
            itemsData: [],
            listHead: [
            {
                name: "排名",
                style: {
                    flex: 1,
                    textAlign: 'center'
                },
                icon:'el-icon-medal-1'
            },
            {
                name: "内容",
                style: {
                    flex: 10,
                },
                icon: 'el-icon-document'
            },
            {
                name: "发帖人",
                style: {
                    flex: 1,
                    textAlign: 'center'
                },
                icon:'el-icon-user'
            },            
            {
                name: "评论数",
                style: {
                    flex: 1,
                    textAlign: 'center'
                },
                icon: 'el-icon-chat-dot-round'
            },
            {
                name: "点赞数",
                style: {
                    flex: 1,
                    textAlign: 'center'
                },
                icon:'el-icon-thumb'
            },
            {
                name: "转发数",
                style: {
                    flex: 1,
                    textAlign: 'center'
                },
                icon:'el-icon-share'
            }
            ],
            leftData: [
                {
                    name: "曝光量",
                    value: 0,
                    unit: "次",
                },
                {
                    name: "真实性",
                    value: 0,
                    unit: "百分比",
                },
                {
                    name: "积极情感值",
                    value: 0,
                    unit: "百分比",
                },
                {
                    name: "参与用户人数",
                    value: 0,
                    unit: "人",
                },
            ],
        };
    },
    mounted() {
        this.getData('zhihu')
        this.tupu(0)
    },
    beforeDestroy () {
        this.myChart.clear() 
        // this.getData('weibo')
        // this.tupu(0)            
    },     
    methods: {
        tupu(index){
            console.log('index',index)    
            var chartDom = document.getElementById('tupu');
            this.myChart =  this.$echarts.init(chartDom);
            var size
            if(index==1){
               size=500
                console.log('index==1')    
            }
            else{
                size=20
            }
            this.axios.get(this.baseUrl+'/yilan-json/effect/hot_upper.json').then((res)=>{
                var data = res.data[index].data
                var itemList =[]
                var colorList = [[
                    '#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
                    '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
                    '#1e90ff', '#ff6347', '#7b68ee', '#d0648a', '#ffd700',
                    '#6b8e23', '#4ea397', '#3cb371', '#b8860b', '#7bd9a5'
                    ],
                    [
                    '#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
                    '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
                    '#1e90ff', '#ff6347', '#7b68ee', '#00fa9a', '#ffd700',
                    '#6b8e23', '#ff00ff', '#3cb371', '#b8860b', '#30e0e0'
                    ],
                    [
                    '#929fff', '#9de0ff', '#ffa897', '#af87fe', '#7dc3fe',
                    '#bb60b2', '#433e7c', '#f47a75', '#009db2', '#024b51', 
                    '#0780cf', '#765005', '#e75840', '#26ccd8', '#3685fe', 
                    '#9977ef', '#f5616f', '#f7b13f', '#f9e264', '#50c48f'
                    ]][2];                
                for(var i=0;i<40; i++){
                    var colorIndex=parseInt(Math.random()*17) 
                    var item={
                        "name": data[i].name,
                        "value":data[i].thumbUp,
                        "symbolSize":parseInt( data[i].thumbUp/size) ,
                        "article":data[i].article,
                        "rank":data[i].rank,
                        "draggable": true,
                        "itemStyle": {
                            "normal": {
                                "shadowBlur": 100,
                                "shadowColor": colorList[colorIndex],
                                "color": colorList[colorIndex ]
                            }
                        }
                    }
                    itemList.push(item)                    
                }
                this.myChart.on('click', function(params) {
                    window.open(params.data.url);
                });
                var option = {
                    // 图表标题
                    title: {
                        show:true,//显示策略，默认值true,可选为：true（显示） | false（隐藏）
                        text: '意见领袖图谱',//主标题文本，'\n'指定换行
                        x: 'center',        // 水平安放位置，默认为左对齐，可选为：
                                        // 'center' ¦ 'left' ¦ 'right'
                                        // ¦ {number}（x坐标，单位px）
                        y: 'top',             // 垂直安放位置，默认为全图顶端，可选为：
                                        // 'top' ¦ 'bottom' ¦ 'center'
                                        // ¦ {number}（y坐标，单位px）
                        //textAlign: null          // 水平对齐方式，默认根据x设置自动调整
                        backgroundColor: 'rgba(0,0,0,0)',
                        borderColor: '#ccc',    // 标题边框颜色
                        borderWidth: 0,         // 标题边框线宽，单位px，默认为0（无边框）
                        padding: 5,             // 标题内边距，单位px，默认各方向内边距为5，
                                                // 接受数组分别设定上右下左边距，同css
                        itemGap: 10,            // 主副标题纵向间隔，单位px，默认为10，
                        textStyle: {
                            fontSize: 18,
                            fontWeight: 'bolder',
                            color: 'white'        // 主标题文字颜色
                        },
                        subtextStyle: {
                            color: 'white'        // 副标题文字颜色
                        }
                    },
                    // backgroundColor: '#fff',
                    tooltip: {
                        trigger: 'item',
                        formatter: v => {
                            
                            return  `
                            <div class='u-p-2'>
                                <div class='fz-10'>点赞数：${v.data.value}</div>
                                <div class='fz-10 u-mt-2'>疫情相关帖子数：${v.data.article}</div>
                                <div class='fz-10 u-mt-2'>排名：${v.data.rank}</div>
                            </div>
                            `
                        },
                        axisPointer: {
                            type: 'shadow'
                        },                         
                    },
                    animationDurationUpdate: function(idx) {
                        // 越往后的数据延迟越大
                        return idx * 100;
                    },
                    animationEasingUpdate: 'bounceIn',
                    color: ['#fff', '#fff', '#fff'],
                    series: [{
                        type: 'graph',
                        layout: 'force',
                        force: {
                            repulsion: 500,
                            edgeLength: 10
                        },
                        roam: true,
                        label: {
                            normal: {
                                show: true
                            }
                        },
                        data: itemList
                    }]
                }            
                option && this.myChart.setOption(option);                
            })                      
        },
        getData(id){
            this.axios.get(this.baseUrl+'/'+id+'Rank.json').then((res)=>{
                var data = []
                for(var i=0; i<20; i++){
                    data.push(res.data[i])
                }
                this.loading=false
                this.itemsData=data
            }).catch((err)=>{
            })
        },
        handleClick(item) {
            this.loading=true
            this.platform=item.name
            this.listShow=false
            this.getData(item.id)
            this.tupu(item.index)
        },     
        // amount() {
        //     var chartDom = document.getElementById("main");
        //     var this.myChart = this.$echarts.init(chartDom);
        //     var option;

        //     option = {
        //         xAxis: {
        //             type: "category",
        //             data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        //         },
        //         yAxis: {
        //             type: "value",
        //         },
        //         series: [
        //             {
        //                 data: [820, 932, 901, 934, 1290, 1330, 1320],
        //                 type: "line",
        //                 smooth: true,
        //             },
        //         ],
        //     };

        //     option && this.myChart.setOption(option);
        // },
    },
};
</script>

<style lang='scss' scoped>
.medal{
    position: absolute;
    top: 50%;
    transform: translate(-30%, -50%);
}
.bottom {
    margin-bottom: 36.1px !important;
    height: 117px;
}
.effect-list {
flex:1.5
}
.el-link{
    width: 100%;
    color:#afafaf;
    /deep/span{
        width: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }     
}
</style>