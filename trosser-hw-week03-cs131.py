#	This program prints the result of a few calculations, using data gathered and made available in 
#	the program by manually assigning values to variables (names) which are then used to calculate 
#	the required information.  
#
#	The requirements state "Write a program to determine exactly what 
#	portion of the global population currently has representation (permanent or impermanent) on the 
#	United Nations Security Council. Make sure to cite the sources of the figures you use & peer 
#	review, both due 2/22.
#
# Logic: 
#	Determine countries on the UN Security Council.  
#	Identify the set of permanent member countries, 
#	Identify the set of non-permanent member countries, 
#	Find most recent estimate of population for: 
#		each member country and assign value to a variable,
#		each non-member country and assign value to a variable,
#		the global population and assign value to a variable.
#	Sum the populations for all the member countries in a single variable 'member_countries-total_population'
#	Sum the populations for all the non-permanent countries in a variable 'non_-memeber_coutnries- total_population'
# 	Calculate the portion of the global poopluation currently having representation on the UN Security Council, both for permanent and 
# 	for non-peranent.  
#
#The source of data is as follows: 
#	UN Security Council Permanent and Non-Permanent countries: the UN website.  URL: 
#		https://main.un.org/securitycouncil/en/content/current-members
#	Current population estimate of each country: World DataBank, estimates for year 2024  URL:
#		https://databank.worldbank.org/reports.aspx?source=2&country=WLD

#the following population counts were extracted from the World Bank Group DataBank of World Development Indicators.  


total_global_pop = 8141808945

#permanent member coutries and their popluations from same source

china_pop =1408975000
russia_pop = 143533851
us_pop = 340110988
uk_pop = 69226000
france_pop = 68551653

#non-permanent member coutries and their popluations from same source

bahrain_pop = 1588670
colombia_pop = 52886363
congo_pop = 109276265
denmark_pop = 5976992
greece_pop = 10405134
latvia_pop = 1866124
liberia_pop = 5612817
pakistan_pop = 251269164
panama_pop = 4515577
somalia_pop = 19009151

print('  ')
print('  ')
print('  ')
print("Ever wondered what percentage of the world's popoulation is represented on the powerful UN Security Council?")
print('... it is suprizing small ...')
print('  ')
print('  ')

print("Let's break it down.  First we'll need to know how many of us there are, or were, at some point in time.  We'll use 2024:") 
print('  ')

print('The total world estimated population in 2024, per the World Bank Group, was: ', format(total_global_pop, ","))
print('  ')
print('  ')


print('The UN Security Council is comprised of 5 permanent members, and 10 rotating non-permanent members.')
print('  ')
print('  ')
print('  ')
print('The 5 permanent members are China, The Russian Federation, the United States, the United Kindom, and France.')

perm_members_total_pop = china_pop + russia_pop + us_pop + uk_pop + france_pop

print('The sum/total popualation of the 5 permanent member countries (as of 2024) was: ', format(perm_members_total_pop, ","))
print('  ')
print('  ')
print('The 10 non-permanent members are Bahrain, Colombia, Republic of Congo, Denmark, Greece, Latvia, Liberia, Pakistan, Panama, and Somalia.')

non_perm_members_total_pop = bahrain_pop + colombia_pop + congo_pop + denmark_pop + greece_pop + latvia_pop + liberia_pop + pakistan_pop + panama_pop +somalia_pop 

print('The sum/total popualation of the 10 non-permanent member countries (as of 2024) was: ', format(non_perm_members_total_pop, ","))
print('  ')
print('  ')
print('  ')

print('The portion of the global population with permanent representation is ', 100*(perm_members_total_pop / total_global_pop),'%')
print('  ')
print('The portion of the global population with non-permanent representation is ', 100*(non_perm_members_total_pop / total_global_pop),'%')
