import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'
export const send_message = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/send_message/',
        params: param
    })
}
export const get_receive_message = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/get_receive_message/',
        params: param
    })
}
export const new_user = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/new_user/',
        params: param
    })
}
export const authentication = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/authentication/',
        params: param
    })
}
export const new_activity = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/new_activity/',
        params: param
    })
}
export const sign_up_activity = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/sign_up_activity/',
        params: param
    })
}
export const get_signed_up_activities = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/get_signed_up_activities/',
        params: param
    })
}
export const join_activity = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/join_activity/',
        params: param
    })
}
export const get_joined_activities = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/get_joined_activities/',
        params: param
    })
}
export const get_all_activities = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/get_all_activities/',
        params: param
    })
}
export const get_activity = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/get_activity/',
        params: param
    })
}
export const search_by_name = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/search_by_name/',
        params: param
    })
}
export const comment = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/comment/',
        params: param
    })
}
export const get_act_comments = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/get_act_comments/',
        params: param
    })
}
export const get_user_comments = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/get_user_comments/',
        params: param
    })
}
export const get_comment_by_id = param => {
    return axios({
        method: 'get',
        url: '/BackEnd/get_comment_by_id/',
        params: param
    })
}
