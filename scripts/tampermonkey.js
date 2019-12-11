// ==UserScript==
// @name         Zendesk articles at GitHub
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  show a link to Zendesk article
// @author       You
// @match        https://github.com/Memsource/zendesk-articles/blob/*.html
// @grant        none
// @require      http://code.jquery.com/jquery-3.4.1.min.js
// @downloadURL  https://raw.githubusercontent.com/Memsource/zendesk-articles/master/scripts/tampermonkey.js
// ==/UserScript==

(function() {
    'use strict';

    var $path = $('.final-path');
    console.log($path);
    var id = $path.text().split(".")[0];
    var link = "https://help.memsource.com/hc/en-us/articles/" + id;
    $path.html("<a target='_blank' href='" + link + "'>Zendesk: " + $path.text() + "</a>");
})();
