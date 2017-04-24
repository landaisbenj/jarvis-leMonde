#!/bin/bash
# Here you can define translations to be used in the plugin functions file
# the below code is an sample to be reused:
# 1) uncomment to function below
# 2) replace XXX by your plugin name (short)
# 3) remove and add your own translations
# 4) you can the arguments $2, $3 passed to this function
# 5) in your plugin functions.sh file, use it like this:
#      say "$(pv_myplugin_lang the_answer_is "oui")"
#      => Jarvis: La réponse est oui

#pv_XXX_lang () {
#    case "$1" in
#        i_check) echo "Je regarde...";;
#        the_answer_is) echo "La réponse est $2";;
#    esac
#} 

jv_leMonde_dayNews()
{
	python -u ~/jarvis/plugins_installed/jarvis-leMonde/python/dayNews.py
	while read line
	do
		say "$line"
	done < ~/jarvis/plugins_installed/jarvis-leMonde/python/news.txt
}

jv_leMonde_news()
{
	python -u ~/jarvis/plugins_installed/jarvis-leMonde/python/news.py
	while read line
	do
		say "$line"
	done < ~/jarvis/plugins_installed/jarvis-leMonde/python/news.txt
}

jv_leMonde_favoriteNews()
{
	python -u ~/jarvis/plugins_installed/jarvis-leMonde/python/favoriteNews.py
	while read line
	do
		say "$line"
	done < ~/jarvis/plugins_installed/jarvis-leMonde/python/favoriteNews.txt
}

jv_leMonde_addFavoriteNews()
{
	python -u ~/jarvis/plugins_installed/jarvis-leMonde/python/addFavoriteNews.py
	while read line
	do
		say "$line"
	done < ~/jarvis/plugins_installed/jarvis-leMonde/python/rubrique.txt
}

jv_leMonde_removeFavoriteNews()
{
	python -u ~/jarvis/plugins_installed/jarvis-leMonde/python/removeFavoriteNews.py
	while read line
	do
		say "$line"
	done < ~/jarvis/plugins_installed/jarvis-leMonde/python/rubrique.txt
}
