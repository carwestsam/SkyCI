import axios from 'axios'

let Axios = axios.create({
    baseURL: 'http://localhost:5000',
    timeout: 3000,
})

export default function getAxios() {
    return Axios
}
