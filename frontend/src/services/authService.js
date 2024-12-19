import axios from 'axios';

const API_URL = 'http://localhost:3000/api';

const login = async (email, password) => {
    const response = await axios.post(`${API_URL}/user/login`, { email, password });
    if (response.data.token) {
        localStorage.setItem('user', JSON.stringify(response.data));
    }
    return response.data;
};

const register = async (name, email, password) => {
    const response = await axios.post(`${API_URL}/user/register`, { name, email, password });
    return response.data;
};

const logout = () => {
    localStorage.removeItem('user');
};

export default {
    login,
    register,
    logout,
};
