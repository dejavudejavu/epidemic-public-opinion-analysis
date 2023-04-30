<template>
    <div class="c-mains c-m-box" style="top: 112px;display:flex;flex-direction:column;">
        <!-- 上 -->
        <div style='flex:1;display:flex;flex-direction:row'>
            <div class=" c-m-flex;" style="margin-right: 30px;flex:1;">
                <c-box style="width: 100%; height: 100%">
                    <template v-slot:main>
                        <div class="c-list-head headtext" style="padding-left: 0">
                            <div style="text-align: center"  class="c-l-title"><span>词汇情感</span></div>
                        </div>
                        <div id="emoPie" class="full-box"></div>
                    </template>
                </c-box>
            </div>
            <div class="c-m-flex-1 c-m-flex" style='display:flex;flex-direction:column;flex:1'>
                <c-box
                    class='lbx'
                >
                    <template v-slot:main>
                        <div class="c-list-head headtext" style="padding-left: 0">
                            <img
                                src="../../public/images/chartbg_head.png"
                                style="float: left; margin-top: 2px"
                            />                        
                            <div style="text-align: center"   class="color-title">情感值变化</div>
                        </div>
                        <div id='bianhua' style='height:92%'></div>
                    </template>
                </c-box>
            </div>
        </div>
<!-- 下 -->
        <div style='display:flex;flex:1'>
            <div style='flex:1' id='ciyunPos'></div>
            <div style='flex:1' id='ciyunNeu'></div>
            <div style='flex:1' id='ciyunNeg'></div>
        </div>
    </div>
</template>

<script>
import 'echarts-wordcloud';
export default {
    data() {
        return {
            texts: {
                title: "新冠",
            },
            base64:[
                'data:image/png;base64,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',
                'data:image/png;base64,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',
                'data:image/png;base64,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',
            ],
            // word: word,
            attackType: 1,
            eventTotals: [],
            deviceTotals: [],
            leftState: 1,
            leftData: [
                {
                    name: "正向高频词",
                    value: 0,
                    unit: "次",
                    img:this.baseUrl+'/posword.png'
                },
                {
                    name: "中性高频词",
                    value: 0,
                    unit: "百分比",
                    img:this.baseUrl+'/neuword.png'
                },
                {
                    name: "负向高频词",
                    value: 0,
                    unit: "百分比",
                    img:this.baseUrl+'/negword.png'                    
                },
            ],
        };
    },
    mounted() {
        var neg
        var neu
        var pos
        this.axios.get(this.baseUrl+'/yilan-json/emotion/EmotionSub.json').then((res)=>{
            
            neg=res.data[0].neg;
            neu=res.data[0].neu;
            pos=res.data[0].pos;   
            this.ciyun('ciyunPos',pos,this.base64[0])
            this.ciyun('ciyunNeu',neu,this.base64[1])
            this.ciyun('ciyunNeg',neg,this.base64[2])
        }) 
        this.emoPie();
        this.bianhua();
    },
    methods: {
        emoPie() {
            var chartDom = document.getElementById("emoPie");
            var myChart = this.$echarts.init(chartDom);
            var img = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGCAYAAACJm/9dAAABS2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxMzggNzkuMTU5ODI0LCAyMDE2LzA5LzE0LTAxOjA5OjAxICAgICAgICAiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIi8+CiA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo8P3hwYWNrZXQgZW5kPSJyIj8+IEmuOgAAE/9JREFUeJztnXmQVeWZxn/dIA2UgsriGmNNrEQNTqSio0IEFXeFkqi4kpngEhXjqMm4MIldkrE1bnGIMmPcUkOiIi6gJIragLKI0Songo5ZJlHGFTADaoRuhZ4/nnPmnO4+l+7bfc85d3l+VV18373n3Ptyvve53/5+da1L6jDdYjgwBhgNHALMBn6Sq0VdcxlwGvACsAx4HliTq0VlRlNzY+LrfTO2o5LoDxwOHAmMA/4WiP+KzM3DqCJpAA4K/i4F2oBXgWbgWWAxsDEv48oZC6M9Q4EJwInAMcDAfM0pOXXA14K/y4FPgQXAfOBxYF1+ppUXFgYMBiYCp6PaoU+B694HFqEmyVJgVSbW9Y6bgCeBb6Am4GHALrH3B6L/+0RgM6pFHgQeAzZkaWi5UVejfYx64AjgXOAk1OToSCtqajyFHGZlVsalzH7oB+BYJJR+Cde0oKbi3cBCYEtWxmVNoT5GrQljGHAecD7wxYT3P0bNirlIEB9lZ1ouDEICOQk1H7dLuOYt4C7gZ8Da7EzLhloXxv7AJcCZdK4dWpAIHkDt7FrtjA5A/aszkFiSntP9wAzgP7M1LT0KCaM+YzuyZixy+leAb9O+sN9AHdDd0S/mbGpXFKD/+2z0LHZHz+aN2PsN6Bm+gjrsY7M2MEuqVRhHoU7yYjS6FPI5MAc4FNgHzUN4JKYz69Cz2Qc9qzno2YUcjZ7t8iBddVSbMEYDzwFPA6Nir28Afgx8CZiERpVM91iKntnfoGcYH606BNUez6GRr6qhWoSxF/AoKsQxsdfXAj9AHe2rgNXZm1Y1/A96hl8E/pn2HfExwBJUBntlb1rpqXRhbA/cDLyGxuJDPgSuBPYErqPGx+RLzAagCT3bK9GzDpmIyuJmVDYVS6UKow74e+APwPeIxuI/AX6Emkw3opldkw6fome8F3rmnwSv90Nl8gdURhU57FmJwtgHdfx+jpZwgCag7gW+DFyDa4gsWY+e+ZdRGYSTgUNRGS1GZVZRVJIwtgF+iMbQ4/2IF4ADgHOA93Kwy4j3UBkcgMokZAwqsx+iMqwIKkUYI4AXgelEzab1wAVoNOSVnOwynXkFlckFqIxAZTYdleGInOwqinIXRh1wMfASMDL2+hxgb+BOqngdTwWzBZXN3qisQkaisryYMu97lLMwhgHzgJ+ivRGgIcJJwd8HOdllus8HROUVDu/2R2U6D5VxWVKuwjgEVcnjY689jqrhOYl3mHJmDiq7x2OvjUdlfEguFnVBOQrju2gmdbcgvwmYitbweFtm5bIGleFUVKagMn4OlXlZUU7C6A/MQqs3w9GLN4ADgZloW6apbNpQWR5ItEBxG1Tms4iazLlTLsLYCW2IOTv22iNor3Il7JQzxbEKle0jsdfORj6wUy4WdaAchDEC+A1RW3MzcAVwKtW/UaiW+QiV8RWozEE+8Bu0yzBX8hbGwaiNuUeQ/xi1Q2/CTadaoA2V9Umo7EG+8Dw57/fIUxhHAs8AOwb5t9Cy8fm5WWTyYj4q+7eC/PZoOfspeRmUlzBOBn4FbBvkX0XVaLUEHDDFsxL5wG+DfAOKWHJOHsbkIYwpaAtluLRjEdol5nVO5j20tmpRkO+DAjFclLUhWQvjUhSSJYzdNA84DneyTcRHyCfmBfk64HYUbjQzshTGVOBWojUys9GoREuGNpjKoAX5xuwgXwfcQoY1R1bCmILWx4SimAWcBXyW0febyuMz5COzgnxYc0zJ4suzEMZEFKwrFMVDKAzL5oJ3GCM2I195KMjXIV86Ke0vTlsYR6CRhbBPMReYjEVhus9mNCseRpfvg5pYR6T5pWkKYz8UNSIcfVqIzmpoTfE7TXXyGfKdhUG+H/Kt1GbI0xLGMODXKJI4aIz6m1gUpue0Ih8Kw4MORj6Wyp6ONITRADyBwjyC4hEdjwMUmN6zAUU+fDPI7458LSlafa9IQxh3oZWToP/ICcDbKXyPqU3WouDT4Q/tQcjnSkqphXEJ6lyDOk2T8TIPU3pW0n4QZzLyvZJRSmGMQislQ65C1ZwxafAEioQYchPt4xX3ilIJYygaaw5HoB5BM5XGpMmtwMNBuh/ywaGFL+8+pRBGHYpAF+7R/h2anfR+CpM2bWj1bbhNdjfki70OzVMKYVxEFM1jE955Z7Il3AkYHvoznhKsqeqtML6KIluHfB93tk32rEK+F3Iz8s0e0xth9EXVVhjZ4QkUAcKYPPg3orhV/YH76MVx3b0RxhXA3wXpdehoYPcrTF60oRN5w6PjDkQ+2iN6Kox9UOj3kAtxMDSTP2uQL4ZcA+zbkw/qiTDqULUVTsM/RDRkZkzePEy0TL0B+WrRo1Q9Eca3iEKbrKfEM47GlIBLgP8N0mPQyU5FUawwdqDz7Lajjpty4wPg6lj+RqIwTd2iWGE0Ei3zXUEKi7eMKRF3IR8F+ew1W7m2E8UI4ytEEydbUIRqH9piypWOPnoR8uFuUYwwbiKKQj4LeLmIe43Jg5eJgilsQ/tuwFbprjBGEy37+IT27TdjypmriY5aHo/OB+yS7grjulj6JzhqoKkc3gNui+X/pTs3dUcYRxMNz/4FLyc3lcfNyHdBvnxMVzd0RxiNsfQNeO+2qTw2IN8N6XKEqithjCXaFbUWuKNndhmTOzOJ1lGNoovzN7oSxrRY+jbg057bZUyu/BX1j0OmFboQti6Mkah/AVr64SXlptKZiXwZ5NsjC124NWFcGkvfHftAYyqV9bRfrXFpoQvrWpckLjwcigKl9Qc+B74ErC6hgcbkxR7Af6NNTK3Abk3Njes6XlSoxvgO0c68R7EoTPWwGvk0KLLIBUkXJQmjHu3GC5lRWruMyZ24T58zbdy1nXSQJIxxwJ5B+nVgWentMiZXliHfBvn6kR0vSBJG/JTMu0tvkzFlQdy3O53S1LHzPRht8mhA56DtTjQpYkw1MQR4h8jXd25qbvz/kdeONcZEor3cT2FRmOrlQ3S+Bsjn2x1f1lEYZ8TSD6RolDHlwP2x9JnxN+JNqWHAu2h892NgZ7wExFQ3A4H3ge3QkQK7NjU3roH2NcaJRJHb5mNRmOrnU+TroEMvw8147YQxIZaeizG1QdzXTwwTYVNqAOpoD0Q99GGoOWVMtTMIRTBsQBHThzQ1N24Ma4zDkCgAFmNRmBqhqbnxI+C5IDsAOByiplR85m9BhnYZUw48FUsfCcnCeCYzc4wpD+I+Pw7UxxiOhqzq0HDtbgk3GlOVNDUrpMG0cde+A+yKjhPYuR7F2QknM57PxTpj8ifsZ9QBh9ajYGohS7O3x5iyIL6KfFQ9cHDsBQvD1Cpx3z+4LzAHnV3Whg75M6YWWQVciZpSrYX2fBtTE4Sd746U4pxvY6oOC8OYBCwMYxKwMIxJwMIwJgELw5gELAxjErAwjEnAwjAmAQvDmAQsDGMSsDCMScDCMCYBC8OYBCwMYxKwMIxJwMIwJgELw5gELAxjErAwjEnAwjAmAQvDmAQsDGMSsDCMScDCMCYBC8OYBCwMYxKwMIxJwMIwJgELw5gELAxjErAwjEnAwjAmAQvDmAQsDGMSsDCMScDCMCYBC8OYBCwMYxLoC1wKNABtwC3A5lwtMiYHpo27tg/wPaAOaO0LnAqMCt5fAPw2J9uMyZMRwI+D9PJ6YEXszW9kb48xZUHc91fUA8sKvGlMLTE6ll5eDyxF/QuAMdnbY0xZMDb4tw1YUg+sAVYGL+6K2lrG1AzTxl07Avk+wMqm5sY14XBtc+y6o7I1y5jcift8M0TzGM/E3jgmM3OMKQ+OjaWfBahrXVIHMABYBwwEWoBhwMdZW2dMDgxC3YkGYCMwpKm5cWNYY2wEng7SDcBx2dtnTC4ci3weYEFTc+NGaL8k5IlY+qSsrDImZ+K+/qsw0VEYnwfpE1GzyphqZgDyddBSqMfDN+LCWAssCtLbAeMzMc2Y/DgB+TrAwqbmxjXhGx1X194fS5+WtlXG5MyZsfQD8Tc6CmMuGpUCOB4YkqJRxuTJEOTjIJ9/LP5mR2GsR+IA9dS/lappxuTHZKLRqLlNzY3r428mbVS6N5Y+Ny2rjMmZuG/f2/HNJGE8C7wZpPel/apDY6qB0cBXg/SbBLPdcZKEsQW4J5a/pORmGZMvcZ++p6m5cUvHCwrt+f53ok74N4E9SmyYMXmxB/JpgFbk650oJIx1wOwg3Rf4bklNMyY/LkY+DfBgU3PjuqSLthYl5LZY+lxg+xIZZkxeDAbOi+VvK3Th1oTxCtHCwu2BC3tvlzG5chHRD/wzyMcT6SquVFMsfRleP2Uql4HIh0Ou39rFXQnjOWB5kB4GTO25XcbkylTkwyCfXrSVa7sViXB6LH0VaqcZU0kMRr4b8qOubuiOMBagmgNgR+Dy4u0yJle+j3wX5MtPdXVDd2PX/iCWvhzYpTi7jMmNXVAY2pAfFLowTneFsZRoh9+2dNFxMaaMuB75LMiHl3bnpmKinf8T8FmQngwcUMS9xuTBAchXQb57RXdvLEYYvwNmxu77aZH3G5MlHX10JvBGMTcXw3S0BRbgYNrPIhpTTpyHfBS0xGn6Vq7tRLHC+AtqUoVcD+xU5GcYkzbDad8PvgL5brfpSVPoP4iGb3cA/rUHn2FMmsxAvgnwPPDzYj+gJ8JoQ+umwmXppwGn9OBzjEmDU4gCebQgX20rfHkyPe08/xft22wzUfVlTJ4MB+6I5acDr/fkg3ozqnQj8FKQHgbchc4vMyYP6pAPhj/QLyMf7RG9EcbnwLeBTUF+Al6abvLjQuSDoCbUPxBF1iya3s5DvEb7SZNbgP16+ZnGFMsI4OZY/irkmz2mFBN0twPzg3R/YA4KrW5MFgxCPjcgyD9JCUZKSyGMNmAK8E6Q/wqK0+P+hkmbOhTRZu8g/w5qQhU9CtWRUi3pWIuGyFqD/MnoMHFj0uRyoqmCVuSDawpf3n1KudZpGe1nxW/AEdNNeownOrAe5HvLClxbNKVeBDgD+EWQ7gPMwp1xU3r2Q77VJ8j/AvleyUhjdex5wItBejA6pWb3FL7H1CbD0AEv4RbrF0lhMWsawtiExpPfDvJfAH6N94qb3jMYhXTaM8i/jXxtU6Ebekpa+ynWoLMHNgT5/YBHgX4pfZ+pfvohH9o/yG9APlaSznZH0txotBLFCA1Hqo5AYT8tDlMs2yDfOSLItyLfWpnWF6a9A28hcBY6+A90Qma802RMV/RBnevwdNXN6IiwhWl+aRZbUx8GvkM06TIJuA+Lw3RNH+Qrk4J8G3A+8EjaX5zVnu170JkEoTgmA79EVaQxSWyDaoowmEEb8qFOpx+lQZbBDG5HM5WhOE4DHsJ9DtOZfsg3Tg/ybSho2u1ZGZB1lI/bUFUY73M8hRcdmohBaCFg2KdoQ+ez3JqlEXmEv7mb9uuqDkd7yB3d0OyMfCEcfdqMfkjvKHhHSuQVF+oR4ETgr0F+fxSB2stHapcRwAtE8xQtwBnohzRz8gyY9gxwJFFYkz3RIrAT8jLI5MYJ6IdxzyC/HjgO7bPIhbwjCa4ADgNWB/ntgHlopaT3c1Q/dahTPQ+VPcgXxtLF+RVpk7cwQLOXB6FqFDR2fSPeCVjthDvvbiKa01qBfOHVvIwKKQdhALyPOly/jL12Mlo5OSIXi0yajEBle3LstfvRQMz7uVjUgXIRBmiF5NnAPxJFVd8bhei5CDetqoE6VJYvEW1H/QyV+VmksEq2p5STMEJmoF+OcA95fzRcNxcHdatkhqMyvAOVKaiMD6PEm4xKQTkKAzQ6NRJtcgqZgPojp+ZikekNp6CymxB7bT4q4+WJd+RMuQoDFGBhPKpmwyp2OFoqMBtHWa8EhgMPok52WNtvQjPZE4iOlCg7ylkYoOUAM4ADaX9Y+SQUP/d8yv//UIvUo7J5gyjAMqgMD0Rrnnod4iZNKsWpVqFhvEaipSQ7AHcCS1CVbMqDkahM7iQKxd+Kyu4gVJZlT6UIAzR6MZ3owYeMQgF878HrrfJkF1QGL6MyCQl/uKYTjTaWPZUkjJDX0czoFHSEFOj/MQX4PXAtDryQJYPRM/89KoPQp9YF+bH0MBR/nlSiMEDt0/vQWPhMoqjW2wLXAH9Ey0oG5mJdbTAQPeM/omceHhn8OSqTfVAZlXVfohCVKoyQD4GpwNdQiJ6QoWhZyZ+BaXhpSSkZhJ7pn9EzHhp770lUFlOJavOKpNKFEfI6WqF5KO37H8OB69DCtBtQjCvTM76ADnxcjZ5pfLJ1CXr2x1OBzaYkqkUYIUuBMcAxRIsSQe3gK4E/oTmQ0dmbVrGMRs/sT+jciXj/bQVwLHrmS7M3LT2qTRghT6ORkcODdEhfNAeyFB0schmwY+bWlT9D0LN5DT2rSejZhTyNnu0hwILMrcuAahVGyGJUe3wdHWnbEntvX7SP+F3gMbTUZAC1ywAkgMfQGqZb0TMKaUHP8OvomS7O1rxsqWtdUlOLVoejGdnzgD0S3v8IreGZi4I0fJydabmwHWoKTUR9tKRBitXo0MefkVI4zDxpam5MfL3WhBFSj/Z/nI/W7DQkXNOCdpE9jbbhVsSMbTcYARwFHI2aQ4X+748jQTQDWzKzLmMKCaNv4qvVzxbg2eBve/SLeTowjmg3WQP6NT02yL+Lmg/Lgr9VRGGAypU+SAijg7/DgF0LXLsZiWA2Cp68PgP7ypZarTEKMQzVIOPRr+rWJgivRkPA5cxVaIi1EJ+i2vAJVEOU7WrXtHCN0T3WovU+96DO6OEoksk4FNqn0n9F2tC+iGZUWy4CNuZqUZliYRRmI5pND2fUd0JDwKPRMGVLgfvKiRa0EegF1PxbDnyQq0UVwv8BNYmwIpIWBvwAAAAASUVORK5CYII=';
            this.axios.get(this.baseUrl+'/yilan-json/emotion/emotion.json').then((res)=>{
                var trafficWay=res.data
                var data = [];
                var color=['#ff5b00','#00ffff','#006ced','#ff3000','#00cfff','#ffe000','#ffa800']
                for (var i = 0; i < trafficWay.length; i++) {
                    data.push({
                        value: trafficWay[i].value,
                        name: trafficWay[i].name,
                        itemStyle: {
                            normal: {
                                borderWidth: 5,
                                shadowBlur: 20,
                                borderColor:color[i],
                                shadowColor: color[i]
                            }
                        }
                    }, {
                        value: 2,
                        name: '',
                        itemStyle: {
                            normal: {
                                label: {
                                    show: false
                                },
                                labelLine: {
                                    show: false
                                },
                                color: 'rgba(0, 0, 0, 0)',
                                borderColor: 'rgba(0, 0, 0, 0)',
                                borderWidth: 0
                            }
                }
                    });
                }
                var seriesOption = [{
                    name: '',
                    type: 'pie',
                    clockWise: false,
                    radius: [105, 109],
                    hoverAnimation: false,
                    itemStyle: {
                        normal: {
                            label: {
                                show: true,
                                position: 'outside',
                                color: '#ddd',
                                formatter: function(params) {
                                    var percent = 0;
                                    var total = 0;
                                    for (var i = 0; i < trafficWay.length; i++) {
                                        total += trafficWay[i].value;
                                    }
                                    percent = ((params.value / total) * 100).toFixed(0);
                                    if(params.name !== '') {
                                        return '情感类别：' + params.name + '\n' + '\n' + '占百分比：' + percent + '%';
                                    }else {
                                        return '';
                                    }
                                },
                            },
                            labelLine: {
                                length:30,
                                length2:100,
                                show: true,
                                color:'#00ffff'
                            }
                        }
                    },
                    data: data
                }];
                var option = {
                    backgroundColor: 'rgba(1,42,53,0.8)',
                    color : color,
                    title: {
                        text: '情感占比',
                        top: '48%',
                        textAlign: "center",
                        left: "49%",
                        textStyle: {
                            color: '#fff',
                            fontSize: 22,
                            fontWeight: '400'
                        }
                    },
                    graphic: {
                    elements: [{
                        type: "image",
                        z: 3,
                        style: {
                            image: img,
                            width: 178,
                            height: 178
                        },
                        left: 'center',
                        top:  'center',
                        position: [100, 100]
                    }]
                    },
                    tooltip: {
                        show: false
                    },
                    legend: {
                        icon: "circle",
                        orient: 'vertical',
                        // x: 'left',
                        data:['积极','消极','中性'],
                        right: 10,
                        bottom: 150,
                        align: 'right',
                        textStyle: {
                            color: "#fff"
                        },
                        itemGap: 20
                    },
                    toolbox: {
                        show: false
                    },
                    series: seriesOption
                }
                option && myChart.setOption(option);                   
            })
            // var trafficWay = [{
            //     name: '正向',
            //     value: 20
            // },{
            //     name: '负向',
            //     value: 10
            // },{
            //     name: '中性',
            //     value: 30
            // }];
             

        },
        bianhua(){
            var chartDom = document.getElementById("bianhua");
            var myChart = this.$echarts.init(chartDom);
            this.axios.get(this.baseUrl+'/yilan-json/emotion/EmotionChange.json').then((res)=>{
                var data=res.data.data
                var value=res.data.value
                var temp=[]
                for(var i=0;i<data.length; i++){
                    var id=parseInt(data[i].substring(data[i].length - 4).replace(/\./,""))
                    var item={
                        riqi:data[i],
                        zhi:(value[i]*100).toFixed(0),
                        id:id
                    }
                    temp.push(item)
                }
                temp.sort(function(a,b){
                    return a.id - b.id
                })

                data=[]
                value=[]
                for (i=0;i<temp.length;i++) {
                    data.push(temp[i].riqi)
                    value.push(temp[i].zhi)
                }
                var add={
                    '2021.03.19':'#2021疫情防控进行时#【巴基斯坦总理接种中国新冠疫苗已有60多个国家授权使用中国疫苗】中国新冠疫苗，助力全球抗疫。',                    
                    "2021.03.26":'大学的时候经常发状态，一般情况都是记录自己高兴或者委屈的事情，如今很少发状态了。今天破格发一条，是想纪念打新冠疫苗的事情',
                    "2021.03.22":'【目前监测到的#新冠疫苗接种不良反应有哪些#？专家回应】#关注新冠肺炎#中国疾控中心免疫规划首席专家王华庆：新冠疫苗和既往已用的上市疫苗同类品种相比，结果是类似的。',
                    "2021.04.09":'钟南山院士呼吁：“只有接种疫苗，才能得到比较好的保护。”尽快接种疫苗，加快构筑免疫屏障，让我们一起苗苗苗苗苗！',
                    "2021.03.30":'3月30日，云南省瑞丽市再次发现本土病例。接种新冠病毒疫苗是阻断病毒传播、保护个人健康最有力的措施。'
                }
                
                var option; 
                option = {
                    backgroundColor: 'rgba(1,42,53,0.8)',
                    title: {
                        text:'注:情感值=（积极情感占百比-消极情感占比）*100',
                        textStyle: {
                            color:'#61656f',
                            fontFamily:'等线',
                            fontSize: 15,                        
                        },
                        top: '2%',
                        right: '5%',
                    },
                    // legend: {
                    //     color: ["#17B4FA", "#47D8BE", "#F9A589"],
                    //     // data: ['情感值越大代表正向情感占比越大'],
                    //     left: 'center',
                    //     top: "8%",
                    //     textStyle: {
                    //         color: "#ffffff"
                    //     }
                    // },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            lineStyle: {
                                color: {
                                    type: 'linear',
                                    x: 0,
                                    y: 0,
                                    x2: 0,
                                    y2: 1,
                                    colorStops: [{
                                        offset: 0,
                                        color: 'rgba(0, 255, 233,0)'
                                    }, {
                                        offset: 0.5,
                                        color: 'rgba(255, 255, 255,1)',
                                    }, {
                                        offset: 1,
                                        color: 'rgba(0, 255, 233,0)'
                                    }],
                                    global: false
                                }
                            },
                        },
                        formatter:v=> {
                            var id=v[0].dataIndex
                            var result
                            if(data[id] in add){
                                result =`
                                    <div class='u-p-2' style='width:400px'>
                                        <div class='fz-10'>${data[id]}</div>
                                        <div style='font-weight: bold;font-size:20px'><span style="color:#3CDDCF">●</span><span></span>情感值：${value[id]}</div>
                                        <div class='fz-10 u-mt-2' style='white-space:normal; word-break:break-all;overflow:hidden;'>事件：${add[data[id]]}</div>
                                    </div>                                        
                                `
                                // add[data[id]]
                            }
                            else{
                                result=`
                                    <div class='u-p-2'>
                                        <div class='fz-10'>${data[id]}</div>
                                        <div style='font-weight: bold;font-size:20px'><span style="color:#3CDDCF">●</span>情感值：${value[id]}</div>
                                    </div>                                        
                                `
                            }
                            return result
                        },                          
                    },
                    grid: {
                        top: '15%',
                        left: '5%',
                        right: '5%',
                        bottom: '15%',
                        // containLabel: true
                    },
                    xAxis: [{
                        type: 'category',
                        axisLine: {
                            show: true,
                            lineStyle: {
                                color: '#9581F5'
                            },
                        },
                        splitArea: {
                            // show: true,
                            color: '#f00',
                            lineStyle: {
                                color: '#f00'
                            },
                        },
                        axisLabel: {
                            color: '#fff'
                        },
                        splitLine: {
                            show: false
                        },
                        boundaryGap: false,
                        data: data,

                    }],
                    yAxis: [{
                        type: 'value',
                        min: 0,
                        // max: 140,
                        splitNumber: 4,
                        splitLine: {
                            show: true,
                            lineStyle: {
                                color: 'rgba(255,255,255,0.1)'
                            }
                        },
                        axisLine: {
                            show: true,
                            lineStyle: {
                                color: '#9581F5'
                            },
                        },
                        axisLabel: {
                            show: true,
                            margin: 20,
                            textStyle: {
                                color: '#d1e6eb',

                            },
                        },
                        axisTick: {
                            show: true,
                        },
                    }],
                    dataZoom: [{
                        show: true,
                        height: "5%",
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
                    series: [{
                            name: '情感值',
                            type: 'line',
                            // smooth: true, //是否平滑
                            showAllSymbol: true,
                            // symbol: 'image://./static/images/guang-circle.png',
                            symbol: 'circle',
                            symbolSize: 25,
                            lineStyle: {
                                normal: {
                                    color: "#6c50f3",
                                    shadowColor: 'rgba(0, 0, 0, .3)',
                                    shadowBlur: 0,
                                    shadowOffsetY: 5,
                                    shadowOffsetX: 5,
                                },
                            },
                            label: {
                                show: true,
                                position: 'top',
                                textStyle: {
                                    color: '#6c50f3',
                                }
                            },
                            itemStyle: {
                                color: "#6c50f3",
                                borderColor: "#fff",
                                borderWidth: 3,
                                shadowColor: 'rgba(0, 0, 0, .3)',
                                shadowBlur: 0,
                                shadowOffsetY: 2,
                                shadowOffsetX: 2,
                            },
                            tooltip: {
                                show: true
                            },
                            areaStyle: {
                                normal: {
                                    color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                            offset: 0,
                                            color: 'rgba(108,80,243,0.3)'
                                        },
                                        {
                                            offset: 1,
                                            color: 'rgba(108,80,243,0)'
                                        }
                                    ], false),
                                    shadowColor: 'rgba(108,80,243, 0.9)',
                                    shadowBlur: 20
                                }
                            },
                            data: value
                        },
                        
                    ]
                };   
                option && myChart.setOption(option);                     
            })

           
        },
        ciyun(id,item,img){
            var chartDom = document.getElementById(id);
            var myChart = this.$echarts.init(chartDom); 
            var symbolUrl =img
            var data =item;
            var maskImage = new Image();
            var title=''
            if(id=='ciyunPos'){
                title='积极词云图'
            }else if(id=='ciyunNeu'){
                title='中性词云图'
            }else{
                title='消极词云图'
            }
            maskImage.onload = function() {
                myChart.setOption({
                    title: {
                        text:title,
                        textStyle: {
                            color:'white',
                            fontFamily:'等线',
                            fontSize: 20,                        
                        },
                        bottom: '0.01%',
                        right: 'center',
                    },                    
                    tooltip: {
                        show: false
                    },
                    grid: {
                        left: 0,
                        bottom: 0,
                        top: 0,
                        right: 0,
                    },
                    xAxis: {
                        type: "category",
                        show: false
                    },
                    yAxis: {
                        // max: 100,
                        show: false
                    },
                    textStyle: {
                        normal: {
                            color: function() {
                                return 'rgb(' + [
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160)
                                ].join(',') + ')';
                            }
                        },
                    },                    
                    series: [
                        {
                            type: 'wordCloud',
                            sizeRange: [10, 100],
                            rotationRange: [-30, 30],
                            maskImage: maskImage,
                            textPadding: 0,
                            gridSize: 5,
                            width: '120%',
                            height: '120%',
                            left: 'center',
                            top: 'center',
                            bottom: 25,
                            drawOutOfBound: false,
                            data: data
                        },
                    ]
                });
            };
            maskImage.src = symbolUrl;             
        }
      
    },
}
</script>

<style scoped>
.bottom {
    margin-bottom: 11.1px !important;
    height: 305.6px;
    width: 100%;
}
.lbx{
    flex:1;
}
.no-margin{
    margin:0
}
</style>


