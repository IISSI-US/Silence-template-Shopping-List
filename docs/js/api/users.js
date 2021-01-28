'use_strict';

import { BASE_URL, requestOptions } from './common.js';

const usersAPI = {

    getAll: function () {
        return new Promise(function (resolve, reject) {
            axios
                .get(`${BASE_URL}/users`, requestOptions)
                .then(response => resolve(response.data))
                .catch(error => reject(error.response.data.message));
        });
    },
};

// The export keyword creates a new javascript module
export { usersAPI };