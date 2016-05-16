function setupChoiceController() {
	getSavedData('METHOD',function(items,key) {
		if(items!==null && typeof items[key]!=='undefined') {
			document.getElementById(items[key]).checked = true;
		} else {
			document.getElementById('tfidf2').checked = true;
		}
	});
    getSavedData('THRESHOLD',function(items,key) {
        if(items!==null && typeof items[key]!=='undefined') {
            document.getElementById('thresholdinput').value = items[key];
        } else {
            document.getElementById('thresholdinput').value = 30;
        }
    });
	// Inline functions like onclick aren't allowed.
	document.addEventListener('click',function() {
		var target = event.target;
		if(hasClass(target,'save-button')) {
            saveThresholdPercentage();
			changeChoice();

		}
	});
}

function saveThresholdPercentage() {
    var checkedItem = document.getElementById("thresholdinput");
    setSavedData('THRESHOLD',checkedItem.value);
}

function changeChoice() {
	var checkedItem = document.querySelector('input[name="method"]:checked');
	setSavedData('METHOD',checkedItem.value);
	chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.update(tabs[0].id, {url: tabs[0].url});
    });
}

setupChoiceController();

/**********************************************************************************************************************************/
/**********************************************************************************************************************************/
/**************************************************HELPER FUNCTIONS****************************************************************/
/**********************************************************************************************************************************/
/**********************************************************************************************************************************/
function setSavedData(key, value) {
    var jsonfile = {};
    jsonfile[key] = value;
    chrome.storage.sync.set(jsonfile, function() {
        console.log('Data saved');
    });
}

function getSavedData(key,callback) {
    var key = key || '';
    chrome.storage.sync.get(key, function(items) {
        if(callback!=null) {
            callback(items,key);
        }
        else
            return items[key];
    });
}

function hasClass(el, name) {
   return new RegExp('(\\s|^)'+name+'(\\s|$)').test(el.className);
}

function httpGet(theUrl,body,callback) {
    var xmlHttp = null;
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, true );
    xmlHttp.send();
    xmlHttp.onload = callback;
    return xmlHttp.responseText;
}