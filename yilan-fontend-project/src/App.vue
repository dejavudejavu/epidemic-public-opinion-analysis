<template>
  <div>
    <div class="c-full" style="overflow:hidden">
      <template >
        <div class="index-main">
          <div class="head-pic"></div>
          <!-- head -->
          <div class="c-head" style='overflow: initial;'>
            <!-- 左侧 -->
            <div class="c-head-left c-head-flex">
              <!-- 时间 -->
              <div class="num-font c-head-time">{{time}}</div>
              <!-- 总览 -->
              <div class="f-1" @click="handleClick(0)">
                <div class="head-icon i-b">
                  <img :src=" headMenu[0].imgPath" alt="">
                </div>
                <div class="text i-b">
                  <div :class="[selected===0?'list-title':'word-font']">总览</div>
                </div>
              </div>
              <!-- 传播分析 -->
              <div class="f-1" @click="handleClick(1)">
                <div class="head-icon i-b">
                  <img :src=" headMenu[1].imgPath" alt="">
                </div>
                <div class="text i-b">
                  <div :class="[selected===1?'list-title':'word-font']">传播分析</div>
                </div>
              </div>
            </div>
            <!-- 中间标题 -->
            <div class="c-head-title" style='height: 60px;line-height: 60px; font-size: 50px;padding-top: 8px;'>
              {{ texts.title }}
            </div>
            <!-- 右侧 -->
            <div class="c-head-flex c-head-right">
              <!-- 情感分析-->
              <div class="f-1" style="margin-left: 20px" @click="handleClick(2)">
                <div class="head-icon i-b">
                  <img :src=" headMenu[2].imgPath" alt="">
                </div>
                <div class="text i-b">
                  <div :class="[selected===2?'list-title':'word-font']">情感分析</div>
                </div>
              </div>
              <!-- 影响力分析 -->
              <div class="f-1" @click="handleClick(3)">
                <div class="head-icon i-b">
                  <img :src=" headMenu[3].imgPath" alt="">
                </div>
                <div class="text i-b">
                  <div :class="[selected===3?'list-title':'word-font']">影响力分析</div>
                </div>
              </div>
              <!--  谣言分析-->
              <div class="f-1" @click="handleClick(4)">
                <div class="head-icon i-b">
                  <img :src=" headMenu[4].imgPath" alt="">
                </div>
                <div class="text i-b">
                  <div :class="[selected===4?'list-title':'word-font']">谣言分析</div>
                </div>
              </div>
            </div>
          </div>
          <Overview v-if='selected===0'/>
          <Spread v-if='selected===1'/>
          <Emotiom v-if='selected===2'/>
          <Effect v-if='selected===3'/>
          <Rumor v-if='selected===4'/>
          <div class="c-background"></div>
        </div>  
      </template>
    </div>
  </div>
</template>

<script>
import overview from "../public/images/menuLogo/总览.png";
import spread from "../public/images/menuLogo/标签传播.png";
import emotion from "../public/images/menuLogo/情感.png";
import effect from "../public/images/menuLogo/品牌影响力.png";
import rumor from "../public/images/menuLogo/评论.png";
import Overview from './components/overview'
import Emotiom  from './components/emotion'
import Effect  from './components/effect'
import Rumor from "./components/rumor";
import Spread  from './components/spread'
import dayjs from 'dayjs'


export default {
  name: "App",
  components: {
    Overview,
    Emotiom,
    Effect,
    Rumor,
    Spread
  },
  data() {
    return {
      time:'',
      alertTextContent: "警告",
      overview,
      texts: {
        title: "疫览舆情分析平台",
      },
      headMenu: [
        {
          title: "总览",
          id: 0,
          imgPath: overview
        },
        {
          title: "传播分析",
          id: 1,
          imgPath:spread,

        },
        {
          title: "情感分析",
          id: 2,
          imgPath: emotion,
        },
        {
          title: "影响力分析",
          id: 3,
          imgPath: effect,
        },
        {
          title: "谣言分析",
          id: 4,
          imgPath: rumor,
        },
      ],
      selected: null,
    };
  },
  methods:{
      handleClick(index) {
          this.Storage.set('index',index)
          this.selected=this.Storage.get('index')
      },
  },
  mounted(){
    if(this.Storage.get('index')===null){
      this.selected=0;
      this.Storage.set('index',0)
    }else{
      this.selected=this.Storage.get('index')      
    }
    setInterval(()=>{
      this.time = dayjs().format('YYYY-MM-DD HH:mm:ss');
    }, 1000);
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
