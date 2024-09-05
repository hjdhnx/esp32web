//引入安装好的axios插件
import axios from "axios";
// 查询数据
const get = (url) => {
    return axios.get(url);
};
// 添加数据
const post = (url, data) => {
    return axios.post(url, data);
};
// 修改数据
const put = (url, data) => {
    return axios.put(url, data);
};

// 局部修改
const patch = (url, data) => {
    return axios.patch(url, data);
};

// 删除数据
const del = (url) => {
    return axios.delete(url);
};

//将二次封装好的axios导出
export { get, post, put, del, patch };