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