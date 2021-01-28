'use_strict';

import { BASE_URL, requestOptions } from './common.js';

const listsAPI = {

    getAll: function () {
        return new Promise(function (resolve, reject) {
            axios
                .get(`${BASE_URL}/lists`, requestOptions)
                .then(response => resolve(response.data))
                .catch(error => reject(error.response.data.message));
        });
    },

    getById: function (listId) {
        return new Promise(function (resolve, reject) {
            axios
                .get(`${BASE_URL}/lists/${listId}`, requestOptions)
                .then(response => resolve(response.data[0]))
                .catch(error => reject(error.response.data.message));
        });
    },

    getByUser: function (userId){
        return new Promise(function (resolve, reject) {
            axios
                .get(`${BASE_URL}/lists/${userId}`, requestOptions)
                .then(response => resolve(response.data[0]))
                .catch(error => reject(error.response.data.message));
        });
    },

    delete: function (listId) {
        return new Promise(function (resolve, reject) {
            axios
                .delete(`${BASE_URL}/lists/${listId}`, requestOptions)
                .then(response => resolve(response.data[0]))
                .catch(error => reject(error.response.data.message));
        });
    },

    create: function (formData) {
        return new Promise(function (resolve, reject) {
            axios
                .post(`${BASE_URL}/lists`, formData, requestOptions)
                .then(response => resolve(response.data))
                .catch(error => reject(error.response.data.message));
        });
    },
};

// The export keyword creates a new javascript module
export { listsAPI };