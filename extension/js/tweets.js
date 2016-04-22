console.log('starting tweets.js');

var urlr = chrome.extension.getURL("get_tweets.php");

$(function(){

	$.ajax({
		url: urlr,
		type: 'GET',
		success: function(response) {

			if (typeof response.errors === 'undefined' || response.errors.length < 1) {

				var $tweets = $('<ul></ul>');
				$.each(response, function(i, obj) {
					$tweets.append('<li>' + obj.text + '</li>');
					console.log(obj.text);
				});

				//$('.tweets-container').html($tweets);

			} else {
				//$('.tweets-container p:first').text('Response error');
			}
		},
		error: function(errors) {
			//$('.tweets-container p:first').text('Request error');
		}
	});
});