
/**
* 页面业务逻辑
*/
const leftData = [
    {
        name: "曝光量",
        value: 0,
        unit:'次'
    },
    {
        name: "真实性",
        value: 0, 
        unit:'百分比'
    },    
    {
        name: "积极情感值",
        value: 0, 
        unit:'百分比'
    },
    {
        name: "参与用户人数",
        value: 0,
        unit:'人'
    }
];

const tabs = {
    basic: {
        width: 1
    }
}

const url = "/SOC/webclient/api";
const VM = new Vue({
    el: "#app",
    data() {
        return {
            texts: Config.text || {},
            leftData: leftData,
            listHead: Config.bottomBasic,
            color1: Config.pieColor1,
            color2: Config.pieColor2,
            attackType: 1,

            leftState: 1,

            // 渲染到页面的变量
            modelsShow: false,
            models: [
                {
                    name:"新冠疫情",
                },
                {
                    name: "美国大选",
                },
                {
                    name:"春运",
                },
            ],
            currModel: {
                name:"新冠疫情",
            },

            // 天数
            dayVal: 7,
            days: Config.dayConfig,
            dayShow: false,

            overview: {
                eventAdd: 0, // 今日事件新增
                eventTotal: 0, // 事件总数
                vehicleActive: 0, // 今日活跃车辆
                vehicleAdd: 0, // 今日车辆新增
                vehicleTotal: 0 // 车辆总数
            },

            eventTotals: [],// 事件统计数

            attackTypeChars: [],
            attackEventChars: [],

            itemsData: [
                {
                    comment:"WIFI致癌",
                    date: "2020年1月1日",
                    reliability: "1%",
                    result: "假",
                    resource:"新浪微博"
                },
                {
                    comment:"WIFI致癌",
                    date: "2020年1月1日",
                    reliability: "1%",
                    result: "假",
                    resource:"新浪微博"
                },
                {
                    comment:"WIFI致癌",
                    date: "2020年1月1日",
                    reliability: "1%",
                    result: "假",
                    resource:"新浪微博"
                },
                {
                    comment:"WIFI致癌",
                    date: "2020年1月1日",
                    reliability: "1%",
                    result: "假",
                    resource:"新浪微博"
                },
                {
                    comment:"WIFI致癌",
                    date: "2020年1月1日",
                    reliability: "1%",
                    result: "假",
                    resource:"新浪微博"
                },                {
                    comment:"WIFI致癌",
                    date: "2020年1月1日",
                    reliability: "1%",
                    result: "假",
                    resource:"新浪微博"
                },                {
                    comment:"WIFI致癌",
                    date: "2020年1月1日",
                    reliability: "1%",
                    result: "假",
                    resource:"新浪微博"
                },                {
                    comment:"WIFI致癌",
                    date: "2020年1月1日",
                    reliability: "1%",
                    result: "假",
                    resource:"新浪微博"
                },
            ],
            deviceTotals: [],

            windwoChart: null,
            partsChart: null,

            attackTypeNames: [],
            attackEventNames: [],

            isUpdateList: true,
            updateListNum: 1,

            timeOut: false,

            isAutoCar: false,
            autoTimeout: null,
            modelVal: 0,
            modelValID: null,
            autoQuestData: null,
            alertTime: null,
            alertTextContent:'你有新的信息！'
        }
    },
    create() {


    },
    mounted() {
        // 获取所有car modesl
        // this.getModels().then(res => {
            // 默认选择第一个
        //     let urlParms = this.getRequest();

        //     if (urlParms.model) {
        //         let data = null;
        //         this.models.forEach((elem, i) => {
        //             if (elem.name === urlParms.model) {
        //                 this.modelVal = i;
        //                 data = elem;
        //             }
        //         })
        //         // const data = this.models.filter(elem => elem.name === urlParms.model)[0];
        //         if (data) {
        //             this.clickModel(data);
        //         } else {
        //             this.clickModel(this.models[0]);
        //         }
        //     } else {
        //         this.clickModel(this.models[0]);
        //     }

        //     this.resetQuest();
        // });
        // });
        // 概览统计数 
        // setInterval(() => {
        //     if (this.itemsData.length == 0 || !this.isUpdateList) return false;
        //     const number = this.updateListNum % this.itemsData.length;
        //     this.$refs.list.updateTopEvent(number * 35);
        //     this.updateListNum++;
        // }, Config.listTime)

        _initFlys();

        $("#fly").on("click", () => {
            this.modelsShow = false;
        })
    },
    methods: {

        clickModelItem(item, index) {
            this.modelVal = index;
            this.clickModel(item);
            this.modelsShow = false;
        },
        clickModel(item) {
            // item = { "id": 32, "name": "国六", "tid": 16 };
            if (!item) {
                debugger;
            }
            this.currModel = item;
            // this.modelsShow = false;
            this.modelValID = item.id;
            this.getOverview(item.id);
            // 业务系统安全
            this.getEventDataBusiness(item.id);
            this.getEventDataDevice(item.id);
            this.getEventDataCategory(item.id);
            this.getEventDatas(item.id, 100);
            this.getEventDataGrade(item.id);
            this.getVehicleStatProject(item.id);
        },
        clickDay(val) {
            this.dayVal = val;
            this.dayShow = false;
            this.clickModel(this.currModel)
            this.clickModel(this.currModel, this.modelVal)
        },
        // 获得所有车型
        getModels() {
            return getModels().then(res => {
                this.models = res.map((elem, index) => {
                    return {
                        id: elem.id,
                        name: elem.name,
                        tid: index
                    }
                })
            });
        },
        // 请求获取某车型的概览统计数
        getOverview(id) {
            getOverview(id).then(res => {
                if (this.modelValID != id && this.isAutoCar && this.modelValID != null) return;
                for (const key in res) {
                    if (this.overview.hasOwnProperty(key)) {
                        const elem = res[key];
                        this.overview[key] = elem;
                    }
                }
            });

        },
        // 获取某车型近几日的按业务的事件统计数
        // 业务系统安全
        getEventDataBusiness(id) {
            getEventDataBusiness(id, this.dayVal).then(res => {
                setTimeout(() => {
                    if (this.modelValID != id && this.isAutoCar && this.modelValID != null) return;
                    this.attackWindowChart(res.data);
                });
            });
        },
        // 获取某车型各设备的近几日趋势的事件统计数
        getEventDataDevice(id) {
            const device = [];
            getEventDataDevice(id, this.dayVal).then(res => {
                if (this.modelValID != id && this.isAutoCar && this.modelValID != null) return;
                // 遍历获取零件数

                // 解析成图标所用数据 

                const data = [];
                const XAxio = [];
                res.forEach((elem, i) => {
                    const obj = {
                        data: [],
                        name: elem.name,
                        id: elem.id
                    };
                    data.push(obj);
                    let isShow = false;
                    elem.statData.forEach((_d, x) => {
                        if (i == 0) {
                            const d = parseTime(_d.stateDate);
                            XAxio.push(d);
                        }
                        obj.data.push(_d.total);
                        if (_d.id) {
                            isShow = true;
                        }
                    })
                    elem._show = isShow;
                }) 
                // this.eventTotals = res;



                if (this.partsChart) {
                    this.partsChart.dispose();
                    $("#AttackEvent").html("");
                }
                const options = initLine({
                    data: data,
                    names: XAxio
                })
                this.partsChart = echarts.init(document.getElementById("AttackEvent"));
                this.partsChart.setOption(options);

            });
        },
        // 获取某车型各设备的按攻击类型的事件统计数
        // 攻击类型分布
        getEventDataCategory(id) {
            getEventDataCategory(id, this.dayVal).then(res => {
                if (this.modelValID != id && this.isAutoCar && this.modelValID != null) return;
                this.attackTypeNames = [];
                const data = [];

                res.forEach((elem, i) => {
                    const obj = { data: [], name: elem.name, id: elem.id };
                    let isShow = false;
                    elem.statData.forEach((e, c) => {
                        if (!this.attackTypeNames.includes(e.eventCategory.name)) {
                            this.attackTypeNames.push(e.eventCategory.name);
                        }
                        obj.data.push({
                            name: e.eventCategory.name,
                            value: e.total
                        });
                        if (e.eventCategory.name) {
                            isShow = true;
                        }
                    })
                    obj._show = isShow;
                    data.push(obj)
                });

                console.log(data);

                this.eventTotals = data;

                this.loadAttackType(data);

                const _leftData = [];
                data.forEach((elem) => {
                    let total = 0;
                    elem.data.forEach((child) => {
                        total += child.value;
                    })
                    _leftData.push({
                        name: elem.name,
                        value: total
                    });
                });
                this.leftData = _leftData;
            });
        },
        // 获取某车型各设备的按攻击类型等级的事件统计数
        getEventDataGrade(id) {
            getEventDataGrade(id, this.dayVal).then(res => {
                if (this.modelValID != id && this.isAutoCar && this.modelValID != null) return;
                const data = [];
                this.attackEventNames = [];
                res.forEach((elem, i) => {
                    const obj = { data: [], name: elem.name, id: elem.id };
                    elem.statData.forEach((e, c) => {
                        if (!this.attackEventNames.includes(e.gradeName)) {
                            this.attackEventNames.push(e.gradeName);
                        }
                        obj.data.push({
                            name: e.gradeName,
                            value: e.total
                        })
                    })
                    data.push(obj);
                });
                this.deviceTotals = data;
                
                setTimeout(() => {
                    this.loadAttackEvent(data);
                })

            });
        },
        // 获取某车型各项目车辆统计数
        getVehicleStatProject(id) {
            /*  getVehicleStatProject(id).then(res => { 
             }); */
        },
        // 获取某车型各设备的按攻击类型的事件统计数
        getEventDatas(id, size) {
            getEventDatas(id, size).then(res => {
                if (this.modelValID != id && this.isAutoCar && this.modelValID != null) return;
                let isAlertAttack = false; // 是否提示
                let num = 0;
                clearTimeout(this.alertTime);
                const data = res.map((elem, index) => {

                    // vin
                    let vin = elem.vehicleId;
                    let vinStr = vin;
                    if (String(elem.vehicleId).length > 20) {
                        vinStr = "..." + vinStr.slice(String(vin).length - 20);
                    };

                    const onS = 60 * 1000;
                    if ((elem.eventTime) > Date.now() - onS) {
                        isAlertAttack = true;
                        num ++;
                    }
                    return {
                        id: index + 1,
                        vin: vin,
                        vinStr: vinStr,
                        // 车辆位置
                        province: elem.province,
                        city: elem.city,

                        // 类型
                        code: elem.code,

                        // 攻击类型
                        name: elem.name,
                        // 攻击地址
                        provinceSrc: elem.provinceSrc,
                        citySrc: elem.citySrc,

                        // 攻击IP
                        sip: elem.sip,
                        // 时间
                        eventTime: parseTime(elem.eventTime, true),
                        isActive: (elem.eventTime) > Date.now() - (onS * 10)
                    }
                })
                this.itemsData = data;
                if (isAlertAttack && Config.isAlert) {
                    this.alertTextContent = Config.alertText(num);

                    $(".attck-alert").animate({
                        bottom: "15px"
                    }, 1000); 
                    this.alertTime = setTimeout(() => { 
                        $(".attck-alert").animate({
                            bottom: "-350px"
                        }, 1000);
                    }, Config.alertTime);
                }
            });
        },


        // 加载攻击类型分布
        loadAttackType() {
            // 清除
            this.attackTypeChars.forEach((pie) => {
                pie.dispose();
            })
            this.attackTypeChars = [];
            $("#pies .charts").html("");

            const pies = document.querySelectorAll("#pies .charts");


            setTimeout(() => {
                this.eventTotals.forEach((data, i) => {
                    const elem = document.querySelectorAll("#pies .charts")[i];
                    // if (!data) return false;
                    const popts = initPie(data, 1);

                    var pieChart = echarts.init(elem);

                    pieChart.setOption(popts);
                    this.attackTypeChars.push(pieChart);
                })
            }, 200)


        },
        // 加载攻击事件分布
        loadAttackEvent() {
            this.attackEventChars.forEach((pie) => {
                pie.dispose();
            })
            this.attackEventChars = [];
            $("#pies1 .charts").html("");


            setTimeout(() => {
                this.deviceTotals.forEach((data, i) => {
                    const elem = document.querySelectorAll("#pies1 .charts")[i];
                    // if (!data) return false;
                    const popts = initPie(data, 2);

                    var pieChart = echarts.init(elem);

                    pieChart.setOption(popts);
                    this.attackEventChars.push(pieChart);
                })
            }, 200)
        },
        // 业务系统安全事件
        attackWindowChart(data) {
            //
            if (this.windwoChart) {
                this.windwoChart.dispose();
                $("#windowAttack").html("");
            }
            const opts = data.map((elem) => {
                return {
                    name: elem.name,
                    value: elem.total
                }
            });

            const option = initPictorialBar({
                data: opts,
                height: $("#windowAttack").height()
            }, 2)
            this.windwoChart = echarts.init(document.getElementById("windowAttack"));
            this.windwoChart.setOption(option);
        },
        scrollYEvent() {
            clearTimeout(this.timeOut);
            this.isUpdateList = false;
            this.timeOut = setTimeout(() => {
                this.isUpdateList = true;
            }, Config.listTime);
        },
        tabAuto() {
            clearInterval(this.autoTimeout);
            this.isAutoCar = !this.isAutoCar;
            if (this.isAutoCar) {
                this.resetQuest();
                this.autoTimeout = setInterval(() => {
                    this.updateListNum = 0;
                    this.$refs.list.updateTopEvent(0)
                    this.modelVal = this.modelVal % this.models.length;

                    this.clickModel(this.models[this.modelVal]);
                    this.modelVal++;
                }, Config.carTime);
            }
        },
        getRequest() {
            var url = location.search; //获取url中"?"符后的字串
            var theRequest = new Object();
            if (url.indexOf("?") != -1) {
                var str = url.substr(1);
                strs = str.split("&");
                for (var i = 0; i < strs.length; i++) {
                    theRequest[strs[i].split("=")[0]] = decodeURI(strs[i].split("=")[1]);
                }
            }
            return theRequest;
        },
        resetQuest() {
            clearInterval(this.autoQuestData);

            this.autoQuestData = setInterval(() => {
                this.modelVal = this.modelVal % this.models.length;
                this.clickModel(this.models[this.modelVal], this.modelVal);
            }, Config.dataTime);
        }
    },
    watch: {
        // 切换
        attackType(val) {
            setTimeout(() => {
                if (val == 1) {
                    this.loadAttackType();
                } else {
                    this.loadAttackEvent();
                }
            })

        }
    },
    components: {
        "c-box": borderCom,
        "c-scroll": scrollCom,
    }
})

function _initFlys() {
    var cont_id = "fly"; // 容器id
    var width = 700; // 容器的高
    var height = 479; // 容器的宽
    var config = {
        stats: false, //是否显示左上角的性能监测  默认false
        loading: true, //是否显示 loading ， 默认false
        assets: "",
        scene: {
            offset: [0, 0, 0]
        },
        background: {
            color: '#1E1F22',
            opacity: 0.0,
        }, //背景色和透明度
        camera: {
            width: height,
            height: width
        }, //相机视角和位置
        controls: { //控制器
            enablePan: false,
            enableZoom: false,
            enableRotate: false,
        }
    };


    INT = new INIT_FLY_1602687198755();
    INT.init(cont_id, config); //初始化
    INT.render();
    // 连线数据
    var data = [{
        "data": [
            { "x": -271, "y": 2, "z": -77.50000100003874 }, { "x": -249.07264220144248, "y": 2, "z": -81.46040281592344 }, { "x": -245.660688198683, "y": 2, "z": 3.8384472531063945 }, { "x": -170.77293643413898, "y": 2, "z": -8.907222504662737 }, { "x": -127.77255675647811, "y": 2, "z": 38.39319514078793 }], "id": 1
    },
    { "data": [{ "x": -184.28734147568957, "y": 2, "z": 67.87916977691299 }, { "x": -183.67305033743725, "y": 2, "z": 119.47962539013184 }, { "x": -157.87282253084072, "y": 2, "z": 152.6513468557726 }, { "x": -45.45754423067006, "y": 2, "z": 129.30828360217362 }, { "x": -100.12945553512466, "y": 2, "z": 69.10775205341821 }], "id": 2 },
    { "data": [{ "x": -292.4025818080941, "y": 2, "z": 37.77890400253531 }, { "x": -291.1739995315895, "y": 2, "z": 64.80771408564996 }, { "x": -214.38760725005218, "y": 2, "z": 179.68015693888728 }, { "x": -12.900113903298257, "y": 2, "z": 134.8369038464471 }, { "x": -79.24355683454652, "y": 2, "z": 64.80771408564996 }], "id": 3 },
    { "data": [{ "x": -29.488981457958694, "y": 2, "z": -177.83661367002352 }, { "x": -33.09987714668832, "y": 2, "z": -30.391706380156275 }, { "x": -145.03764349730713, "y": 2, "z": -9.92996414401144 }, { "x": -105.31779092128106, "y": 2, "z": 34.00260006888775 }], "id": 4 },
    { "data": [{ "x": 169.71209737029292, "y": 2, "z": -109.83141153224801 }, { "x": 181.14660038460343, "y": 2, "z": -102.60962015478513 }, { "x": 162.49030599283367, "y": 2, "z": 70.11155695620221 }, { "x": -14.443582754918562, "y": 2, "z": 106.22051384351658 }, { "x": -58.37614696779582, "y": 2, "z": 58.67705394188597 }], "id": 5 },
    { "data": [{ "x": 256.3735938998043, "y": 2, "z": -126.68225807966141 }, { "x": 219.66282106438624, "y": 2, "z": -148.94944816017198 }, { "x": 209.43194994631898, "y": 2, "z": -56.87160809752018 }, { "x": -109.53050255813233, "y": 2, "z": 0.9027229221828782 }, { "x": -83.65241678890325, "y": 2, "z": 30.39170438015631 }], "id": 6 }];
    const data1 = [
        { "data": [{ "x": -134.20495643111818, "y": 2, "z": 41.224391446350694 }, { "x": -173.32299305902262, "y": 2, "z": -2.708172766548561 }, { "x": -251.5590663148314, "y": 2, "z": 14.142673780864866 }, { "x": -253.96633010731782, "y": 2, "z": -72.51882274868977 }, { "x": -266.6044650178715, "y": 2, "z": -70.11155895620215 }], "id": 8 },
        { "data": [{ "x": -110.13231850625397, "y": 2, "z": 67.10247721559269 }, { "x": -56.57069912343098, "y": 2, "z": 125.47862418341764 }, { "x": -155.870330563496, "y": 2, "z": 145.3385504714406 }, { "x": -174.52662495526582, "y": 2, "z": 120.66409659844241 }, { "x": -175.73025685150904, "y": 2, "z": 67.7042931637146 }], "id": 9 }, { "data": [{ "x": -87.26331247763288, "y": 2, "z": 64.69521342310502 }, { "x": -13.841766806796926, "y": 2, "z": 142.931286678953 }, { "x": -218.45918916814307, "y": 2, "z": 189.8729306324617 }, { "x": -300.90797406080304, "y": 2, "z": 66.50066126747076 }, { "x": -302.7134219051679, "y": 2, "z": 38.21531170574111 }], "id": 11 }, { "data": [{ "x": -113.14139824686195, "y": 2, "z": 36.40986386137542 }, { "x": -160.68485814846883, "y": 2, "z": -15.346307677108598 }, { "x": -40.9234844722692, "y": 2, "z": -38.215313705741075 }, { "x": -36.710772835418005, "y": 2, "z": -176.6329817737797 }], "id": 12 }, { "data": [{ "x": -91.47602411448413, "y": 2, "z": 31.595336276400143 }, { "x": -123.97408531305089, "y": 2, "z": -4.5136206109142805 }, { "x": 200.4047107244949, "y": 2, "z": -61.08431973437354 }, { "x": 213.04284563504854, "y": 2, "z": -159.78213522636628 }, { "x": 259.3826736404123, "y": 2, "z": -132.70041756088048 }], "id": 13 }, { "data": [{ "x": -66.1997542933767, "y": 2, "z": 59.88068583812981 }, { "x": -15.045398703040133, "y": 2, "z": 112.84048927285761 }, { "x": 169.71209737029292, "y": 2, "z": 74.92608454117747 }, { "x": 188.36839176206269, "y": 2, "z": -104.41506799915086 }, { "x": 181.14660038460343, "y": 2, "z": -111.63685937661374 }], "id": 14 }]
    INT.initFly(data, {
        style: 5, // 跑点要是
        color: '#ff0000', // 跑点颜色
        size: 2, // 点的大小
        speed: 1, // 速度
        length: 69, // 长度
        dpi: 1 // 密度
    });
    INT.initFly(data1, {
        style: 4, // 跑点要是
        color: '#ffffff', // 跑点颜色
        size: 2, // 点的大小
        speed: 1, // 速度
        length: 120, // 长度
        dpi: 1 // 密度
    });
}