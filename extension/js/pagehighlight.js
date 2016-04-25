var keywords = document.querySelector('[name="keywords"]').getAttribute('content').split(',').join(' ').toLowerCase().split(' ');
var weightUrl = 'http://karanrajpal.in/webskim/sports.php';
keywords.filter(function(item, pos) { 
	if(keywords.indexOf(item)==pos && item.length>0 && item!=='and') {
		return true;
	}
	return false;
});
function highlight() {
	var paras = document.querySelectorAll('p.story-body-text.story-content');
	for (var i = 0; i < paras.length; i++) {
		for (var j = 0; j < keywords.length; j++) {
			var sentences = paras[i].innerHTML.split('. ');
			paras[i].innerHTML = '';
			for (var k = 0; k < sentences.length; k++) {
				if(sentences[k].toLowerCase().indexOf(keywords[j])>0) {
					sentences[k]='<mark>'+sentences[k]+'</mark>';
				}
			}
			paras[i].innerHTML+=sentences.join('. ');
		}
	}
}

highlight();

// httpGet(weightUrl,null,function() {
// 	var response = event.target.responseText;
// 	setSavedData('sports',response);
// });

/* Helper functions */
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
        config[key] = items[key];
        if(callback!=null) {
            callback(items,key);
        }
        else
            return items[key];
    });
}
function httpGet(theUrl,body,callback) {
    var xmlHttp = null;
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, true );
    xmlHttp.send();
    xmlHttp.onload = callback;
    return xmlHttp.responseText;
}