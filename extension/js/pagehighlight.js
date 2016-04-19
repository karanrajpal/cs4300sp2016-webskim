var keywords = document.querySelector('[name="keywords"]').getAttribute('content').split(',').join(' ').toLowerCase().split(' ');
keywords.filter(function(item, pos) { 
	if(keywords.indexOf(item)==pos && item.length>0 && item!=='and') {
		return true;
	}
	return false;
});
var paras = document.querySelectorAll('p.story-body-text.story-content');
for (var i = 0; i < paras.length; i++) {
	for (var j = 0; j < keywords.length; j++) {
		if(paras[i].innerHTML.toLowerCase().indexOf(keywords[j])>0) {
			paras[i].style.background = 'yellow';
			paras[i].style.whiteSpace = 'pre-wrap';
		}
	}
}
// document.getElementsByTagName('p')[2].style.background = 'red';