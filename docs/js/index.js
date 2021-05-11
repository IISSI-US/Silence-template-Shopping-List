"use strict";

import { sessionManager } from './utils/session.js';

import { usersAPI } from '/js/api/users.js';
import { listsAPI } from '/js/api/lists.js';

import { userRenderer } from '/js/renderers/users.js';
import { listRenderer } from '/js/renderers/lists.js';
import { messageRenderer } from '/js/renderers/messages.js';

// DOM elements that we will use
const usersContainer = document.getElementById("users");
const listsContainer = document.getElementById("lists");
const newListBtn = document.getElementById("new-list-button");

// Main function that will run when the page is ready
function main() {
    // Hide the options that shouldn't be available for not logged users
    setLoggedOptions();

    // Load the users
    usersAPI.getAll()
        .then(users => {
            let table = userRenderer.asTable(users);
            usersContainer.appendChild(table);
        })
        .catch(error => messageRenderer.showErrorAsAlert(error));
    
    // Load the lists
    listsAPI.getAll()
        .then(lists => {
            let table = listRenderer.asTable(lists);
            listsContainer.appendChild(table);
        })
        .catch(error => messageRenderer.showErrorAsAlert(error));
}

document.addEventListener("DOMContentLoaded", function () {
    main();
});

///////////

function setLoggedOptions() {
    // Hide the things that shouldnt be available for non authenticated users
    if (!sessionManager.isLogged()) {
        newListBtn.style.display = "none";
    }
}