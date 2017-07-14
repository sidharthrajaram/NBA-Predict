var express = require('express');
var fs = require('fs');
var request = require('request');
var cheerio = require('cheerio');
var app = express();

app.get('/scrape', function(req, res){ //localhost:8081/scrape
	url = 'http://www.imdb.com/title/tt1229340/';

    request(url, function(error, response, html){ //request function with 3 param callback
	    if(!error){
	       	var $ = cheerio.load(html); //jquery functionality 
	        var title, release, rating;
	        var json = { title : "", release : "", rating : ""};

	        $('.header').filter(function(){ //grabs the title and release date
	        	var data = $(this);
	        	title = data.children().first().text();
	        	release = data.children().last().children().text();

	        	json.title = "lol";
	        	json.release = "he";
	        })

	        $(".star-box-giga-star").filter(function(){
	        	var data = $(this);
	        	rating = data.text();
	        	json.rating = "dat way";
	        })

	        fs.writeFile('output.json', JSON.stringify(json, null, 4), function(err){
				console.log('File successfully written! - Check your project directory for the output.json file');
			})

			res.send('Check your console!')
	    }
	})
})

app.listen('8081')

console.log('Magic happens on port 8081');

exports = module.exports = app;
