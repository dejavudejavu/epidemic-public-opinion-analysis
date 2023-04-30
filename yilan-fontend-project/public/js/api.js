// ajax 接口
axios && axios.interceptors.response.use((res) => {
    const result = res || {};
    if (result.status === 200) {
        return result.data;
    }
});

// 对接接口 返回数据
const _url = "/SOC/webclient/api";

const apis = {
    // 获取所有车型
    models: () => _url + "/ss/models",
    // 获取某车型的概览统计数
    overview: (id) => _url + `/ss/model/${id}/overview`,
    // 获取某车型近几日的按业务的事件统计数
    eventDataBusiness: (id, days) => _url + `/ss/model/${id}/eventdataStatBusiness/${days}`,
    // 获取某车型各设备的近几日趋势的事件统计数
    eventDataDevice: (id, days) => _url + `/ss/model/${id}/eventdataStatDevice/${days}`,
    // 获取某车型各设备的按攻击类型的事件统计数
    eventDataCategory: (id, days) => _url + `/ss/model/${id}/eventdataStatDeviceCategory/${days}`,
    // 获取某车型的最新的事件数据
    eventDatas: (id, size) => _url + `/ss/model/${id}/eventdatas/${size}`,
    // 获取某车型各设备的按攻击类型等级的事件统计数
    eventDataGrade: (id, days) => _url + `/ss/model/${id}/eventdataStatGrade/${days}`,
    // 获取某车型各项目车辆统计数
    vehicleStatProject: (id) => _url + `/ss/model/${id}/vehicleStatProject`,
    // 获取某车型各项目事件统计数
    eventdataStatProject: (id, days) => _url + `/ss/model/${id}/eventdataStatProject/${days}`,
    
}

const _promise = (api, opts = {}) => {
    return new Promise((resolve, reject) => {
        axios.get(api, opts).then((res) => {
            resolve(res);
        })
    });
}

// 请求所有车型
function getModels() {
    const api = apis.models();
    return _promise(api).then(res => {
        if (res.success) {
            return res.models
        } else {
            return [];
        }
    });
}
// 请求获取某车型的概览统计数
function getOverview(id) {
    const api = apis.overview(id);
    return _promise(api).then(res => {
        if (res.success) {
            return res.data
        } else {
            return [];
        }
    });
}
// 请求获取某车型的概览统计数
function getEventDataBusiness(id, day) {
    const api = apis.eventDataBusiness(id, day);
    return _promise(api).then(res => {
        if (res.success) {
            return res
        } else {
            return [];
        }
    });
}
// 获取某车型各设备的近几日趋势的事件统计数
function getEventDataDevice(id, day) {
    const api = apis.eventDataDevice(id, day);
    return _promise(api).then(res => {
        if (res.success) {
            return res.data
        } else {
            return [];
        }
    });
}
// 获取某车型各设备的按攻击类型的事件统计数
function getEventDataCategory(id, day) {
    const api = apis.eventDataCategory(id, day);
    return _promise(api).then(res => {
        if (res.success) {
            return res.data
        } else {
            return [];
        }
    });
}
// 获取某车型的最新的事件数据
function getEventDatas(id, size) {
    const api = apis.eventDatas(id, size);
    return _promise(api).then(res => {
        if (res.success) {
            return res.data
        } else {
            return [];
        }
    });
}
// 获取某车型各设备的按攻击类型等级的事件统计数
function getEventDataGrade(id, days) {
    const api = apis.eventDataGrade(id, days);
    return _promise(api).then(res => {
        if (res.success) {
            return res.data
        } else {
            return [];
        }
    });
}
// 获取某车型各项目车辆统计数
function getVehicleStatProject(id) {
    const api = apis.vehicleStatProject(id);
    return _promise(api).then(res => {
        if (res.success) {
            return res.data
        } else {
            return [];
        }
    });
}
// 获取某车型各项目事件统计数
function eventdataStatProject(id, days) {
    const api = apis.eventdataStatProject(id, days);
    return _promise(api).then(res => {
        if (res.success) {
            return res.data
        } else {
            return [];
        }
    });
}