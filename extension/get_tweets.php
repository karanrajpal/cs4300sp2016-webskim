<?php

	require_once('twitter_proxy.php');
	// Twitter OAuth Config options
	$oauth_access_token = '763105153-dHwnEyUXc6dye08ezOGHCBS8axicocUlohDltfVs';
	$oauth_access_token_secret = '	pUgZ48FJR5Od6aqFe0LEXiois48ESvnMQAtNAHDLQlRDr';
	$consumer_key = 'VBiktjQkjgQXIOV4EzDJYT6ht';
	$consumer_secret = 'jHl6J5kZ34VqAVTxa9bz3p0DXF4CgMRk2qtRqQLMenatiwG6Xl';
	$user_id = '763105153';
	$screen_name = 'rcd229';
	$count = 100;
	$twitter_url = 'https://api.twitter.com/1.1/search/tweets.json';
	// Create a Twitter Proxy object from our twitter_proxy.php class
	$twitter_proxy = new TwitterProxy(
		$oauth_access_token,			// 'Access token' on https://apps.twitter.com
		$oauth_access_token_secret,		// 'Access token secret' on https://apps.twitter.com
		$consumer_key,					// 'API key' on https://apps.twitter.com
		$consumer_secret,				// 'API secret' on https://apps.twitter.com
		$user_id,						// User id (http://gettwitterid.com/)
		$screen_name,					// Twitter handle
		$count							// The number of tweets to pull out
	);
	// Invoke the get method to retrieve results via a cURL request
	function console_log( $data ){
		echo '<script>';
		echo 'console.log('. json_encode( $data ) .')';
		echo '</script>';
	}
	$myvar = array(1,2,3);
	console_log($myvar);

	$tweets = $twitter_proxy->get($twitter_url);
	echo $tweets;
?>