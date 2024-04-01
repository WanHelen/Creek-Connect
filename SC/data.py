# data.py

# Create lists

College = [
    {'Name': 'Air Force Academy', 'Information': 'The United States Air Force Academy is a United States service academy in El Paso County, Colorado, immediately north of Colorado Springs. \n\nIt educates cadets for service in the officer corps of the United States Air Force and United States Space Force.', 'Address': 'Air Force Academy, CO 80840', 'Contact': 'Tel: (719) 333-2025 \nEmail: visit@afacademy.af.edu'},
    {'Name': 'CU Boulder', 'Information': "The University of Colorado Boulder (CU Boulder) is a prestigious public research university located in Boulder, Colorado. Known for its strong academic programs, research initiatives, and scenic campus nestled at the foothills of the Rocky Mountains, CU Boulder offers a vibrant and enriching educational experience for students pursuing a wide range of disciplines.", 'Address': 'Boulder, CO 80309', 'Contact': 'Tel: (303) 492-1411'},
    {'Name': 'Colorado State University', 'Information': "Colorado State University (CSU) is a renowned public research university located in Fort Collins, Colorado. With a focus on innovative research, hands-on learning experiences, and a commitment to sustainability, CSU offers a diverse range of academic programs and opportunities for students to excel in their chosen fields.", 'Address': 'Fort Colins, CO 80523', 'Contact': 'Tel: (970) 491-6444 \nEmail: questions@online.colostate.edu'},
    {'Name': 'UCCS', 'Information': "The University of Colorado Colorado Springs (UCCS) is a public research university located in Colorado Springs, Colorado. Recognized for its strong focus on academic excellence, hands-on learning opportunities, and scenic campus nestled against the backdrop of the Rocky Mountains, UCCS provides a dynamic and supportive environment for students pursuing various fields of study.", 'Address': '1420 Austin Bluffs Pkwy, Colorado Springs, CO 80918', 'Contact': 'Tel: (719) 255-8227 \nEmail: go@uccs.edu'},
    {'Name': 'Denver University', 'Information': "The University of Denver (DU) is a private research university located in Denver, Colorado. Known for its strong academic programs, emphasis on experiential learning, and commitment to global engagement, DU provides students with a comprehensive and enriching educational experience in a vibrant urban setting.", 'Address': '2199 S. University Blvd Denver, CO 80210-4711', 'Contact': 'Tel: (303) 871-2000'},
    {'Name': 'Colorado College', 'Information': "Colorado College is a private liberal arts college located in Colorado Springs, Colorado. Renowned for its innovative Block Plan academic schedule, focus on experiential learning, and beautiful mountainous surroundings, Colorado College offers students a unique and personalized educational experience.", 'Address': ' 14 E Cache La Poudre St, Colorado Springs, CO 80903', 'Contact': 'Tel: (719) 389-6000 \nEmail: admissions@coloradocollege.edu'},
    {'Name': 'Colorado School of Mines', 'Information': "The Colorado School of Mines is a public research university specializing in engineering, applied science, and earth sciences, located in Golden, Colorado. Recognized for its rigorous academic programs, hands-on learning opportunities, and strong industry connections, Mines prepares students for successful careers in fields such as energy, mining, environmental science, and more.", 'Address': '1500 Illinois St, Golden, CO 80401', 'Contact': 'Tel: (303) 273-3000'},
    {'Name': 'University of Northern Colorado', 'Information': "The University of Northern Colorado (UNC) is a public research university located in Greeley, Colorado. Known for its strong programs in education, business, and performing arts, UNC offers students a diverse range of academic and extracurricular opportunities in a supportive and engaging campus environment.", 'Address': '501 W 20th St, Greeley, CO 80639', 'Contact': 'Tel: (970) 351-1890 \nEmail: help@unco.edu'},
    {'Name': 'Arizona State University', 'Information': "Arizona State University (ASU) is a public research university located in Tempe, Arizona, with multiple campuses across the Phoenix metropolitan area. Renowned for its innovation, research excellence, and commitment to inclusivity, ASU offers a wide range of academic programs, hands-on learning experiences, and opportunities for students to collaborate with industry partners.", 'Address': '1151 S Forest Ave, Tempe, AZ', 'Contact': 'Tel: (855) 278-5080 \nEmail: customerservice@asu.edu'},
    {'Name': 'University of Arizona', 'Information': "The University of Arizona (UA) is a public research university located in Tucson, Arizona, known for its strong programs in science, engineering, and health sciences. With a focus on innovation, community engagement, and student success, UA offers a diverse range of academic opportunities, research initiatives, and vibrant campus life experiences.", 'Address': '1200 E University Blvd, Tucson, AZ 85721', 'Contact': 'Tel: (520) 621-2211 \nEmail: admissions@arizona.edu'},
    {'Name': 'Pikes Peak Community College', 'Information': "Pikes Peak Community College (PPCC), however, is a public community college located in Colorado Springs, Colorado, offering a variety of academic and vocational programs. Known for its affordable tuition, flexible scheduling options, and supportive learning environment, PPCC serves students seeking career preparation, transfer opportunities, and lifelong learning.", 'Address': '5675 S Academy Blvd, Colorado Springs, CO 80906', 'Contact': 'Tel: (719) 502-2000'},
]


Government = [
    {'Name': 'Academy School District 20', 'Information': "Academy District 20, founded in 1957, is one of the largest school districts in the Pikes Peak Region. With 40 schools, the district serves approximately 26,000 students. We have been Accredited with Distinction, Colorado's highest education performance ranking, every year since the rating's inception.", 'Address': '1110 Chapel Hills Dr, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 234-1200 \nEmail: help@asd20.org'},
    {'Name': "Children's Hospital", 'Information': "As a nationally ranked pediatric hospital, we care for families throughout Colorado and surrounding states. Our comprehensive team of highly trained, experienced specialists sees and treats more children than any other hospital in the region. We give kids the expert care they need to feel better.", 'Address': '4090 Briargate Pkwy, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 305-1234'},
    {'Name': 'UC Health Aspen Creek Medical Center', 'Information': "UC Health’s mission is to improve the health of all people living in Colorado now and in the future, promote health equity through the elimination of health disparities, and reduce barriers to access to clinical, educational, and research programs by creating more inclusive opportunities for employees, students, and trainees.", 'Address': '9480 Briar Village Point Suite 200, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 278-3627'},
    {'Name': 'Colorado Springs Police Department', 'Information': "Our mission is to promote the quality of life in Colorado Springs by providing police services with integrity and with a spirit of excellence, in partnership with our Community.", 'Address': '705 S Nevada Ave, Colorado Springs, CO 80903', 'Contact': '(719) 444-7000'},
    {'Name': 'Colorado Springs Fire Station 19', 'Information': "The Colorado Springs Fire Department, an internationally accredited department, has 24 fire stations and over 500 full time uniformed firefighters. The department has 24 engine companies, 6 truck companies, a heavy rescue team, and a hazardous materials response team.", 'Address': '2490 Research Pkwy, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 385-5950'},
    {'Name': 'Challenger Middle School', 'Information': "At Challenger Middle School, we believe each learner is unique. Students participate in transformative and innovative learning, with a technology emphasis and intentional social skills development. Positive student-teacher relationships help remove obstacles as students prepare for an unimaginable future.", 'Address': '10215 Lexington Dr, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 234-3000'},
    {'Name': 'Mountain View Elementary School', 'Information': "We are a school of innovative learning and technology, that cultivates and empowers each diverse learner in a safe and nurturing environment through transformational and relevant education to become compassionate, globally-minded citizens who strive to continually grow their knowledge, skills, and character while creating a better world, today and in the future.", 'Address': '10095 Lexington Dr, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 234-4800'},
    {'Name': 'DMV', 'Information': "Our mission is to provide motor vehicle, driver and identity services that promote public safety, trust and confidence.", 'Address': '2447 N Union Blvd, Colorado Springs, CO 80909', 'Contact': 'Tel: (303) 205-5694'},
    {'Name': 'Safe2Tell', 'Information': "Safe2Tell is a youth-centered harm prevention and intervention resource for Colorado students and residents, dedicated to improving school and community safety across Colorado since 2004. Safe2Tell's mission is to encourage and empower youth to make a report when a trusted adult isn't available.", 'Address': '1300 Broadway, Denver, CO 80202', 'Contact': 'Tel: (877) 542-7233'},
]


Service = [
    {'Name': 'McDonalds', 'Information': "McDonalds is a global fast food restaurant chain known for its burgers, fries, and beverages. Founded in 1940, it has expanded to thousands of locations worldwide. The company's success is built on efficient operations, iconic branding, and a menu that appeals to a wide range of customers.", 'Address': '1245 Interquest Pkwy \n\nColorado Springs, CO 80921', 'Contact': 'Tel: (719) 424-7678 \nEmail: press@us.mcd.com'},
    {'Name': 'Chick fil A', 'Information': 'Chick-fil-A is a popular American fast-food restaurant chain known for its focus on chicken-based menu items, particularly its signature hand-breaded chicken sandwiches.', 'Address': '7990 N Academy Blvd, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 598-4646 \nEmail: help@chickfila.com'},
    {'Name': 'Taco Bell', 'Information': 'Taco Bell is a fast-food chain specializing in Mexican-inspired cuisine with a menu featuring a variety of tacos, burritos, quesadillas, and other Tex-Mex offerings. ', 'Address': '3436 Research Pkwy, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 268-6861 \nEmail: digitalsupport@tacobell.com'},
    {'Name': 'Raising Canes', 'Information': "Raising Cane's is a fast-food restaurant chain known for its focus on chicken fingers and a limited menu that emphasizes quality and simplicity. Founded in 1996 in Louisiana, Raising Cane's has grown rapidly, expanding across the United States and internationally. The company's success is attributed to its commitment to using fresh ingredients, signature sauce, and providing a straightforward menu that appeals to chicken lovers.", 'Address': '7585 N Academy Blvd, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 593-1599 \nEmail: publicrelations@raisingcanes.com'},
    {'Name': 'Panda Express', 'Information': "Panda Express is a popular fast-casual restaurant chain specializing in American Chinese cuisine, particularly known for its orange chicken dish. Founded in 1983 and headquartered in California, Panda Express has become one of the largest Asian restaurant chains in the United States. The company's menu offers a variety of wok-cooked dishes, sides like fried rice adn chow mein, and a range of sauces to customize flavors, catering to a diverse customer base.", 'Address': '5071 N Academy Blvd, Colorado Springs, CO 80918', 'Contact': 'Tel: (719) 535-0173 \nEmail: PublicRelations@PandaRG.com'},
    {'Name': 'Culvers', 'Information': "Culver's is a fast-food chain known for its focus on fresh frozen custard and ButterBurgers, which are made with fresh beef and butter-toasted buns. Founded in 1984 in Wisconsin, Culver's has expanded across the United States with its signature menu items and commitment to hospitality. The restaurant also offers a variety of other items such as crispy chicken sandwiches, fish sandwiches, and Wisconsin cheese curds, appealing to a wide range of tastes.", 'Address': '7660 N Academy Blvd, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 266-4219 \nEmail: help@culvers.com'},
    {'Name': 'Subway', 'Information': "Subway is a well-known fast-food chain specializing in customizable submarine sandwiches, salads, and wraps. Founded in 1965, Subway has grown into one of the largest restaurant franchises globally, with locations in over 100 countries. The brand is recognized for its emphasis on fresh ingredients, healthy options, and the ability for customers to personalize their meals according to their preferences.", 'Address': '8666 N Union Blvd, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 282-9151 \nEmail: press@subway.com'},
    {'Name': 'Dominos', 'Information': "Domino's is a prominent pizza delivery and takeout chain known for its wide range of pizzas, pasta dishes, and sides. Established in 1960, the company has expanded globally and is recognized for its innovative ordering systems, including online and mobile platforms. Domino's is committed to quality ingredients, fast delivery, and customer satisfaction, making it a popular choice for pizza lovers worldwide.", 'Address': '7055 Lexington Dr, Colorado Springs, CO 80918', 'Contact': 'Tel: (719) 594-0400 \nEmail: media@dominos.com'},
    {'Name': 'Dave & Busters', 'Information': "Dave & Buster's is a restaurant and entertainment chain that combines dining with arcade games and sports viewing experiences. With its first location established in 1982, Dave & Buster's has since grown to become a popular destination for families, friends, and sports enthusiasts seeking a fun and interactive entertainment experience under one roof.", 'Address': '9279 Highland Rdg Hts, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 469-2828 \nEmail: help@daveandbusters.com'},
    {'Name': 'Great Wolf Lodge', 'Information': "Great Wolf Lodge is a family-friendly resort chain known for its indoor water parks, themed suites, and entertainment options for all ages. With multiple locations across North America, Great Wolf Lodge offers a unique vacation experience that combines water park thrills, comfortable accommodations, and various activities such as mini-golf, arcades, and character appearances.", 'Address': '9494 Federal Dr, Colorado Springs, CO 80921', 'Contact': 'Tel: (844) 553-9653 \nEmail: help@greatwolf.com'},
    {'Name': 'Hollywood Theaters', 'Information': "Hollywood Theaters is a cinema chain offering a wide range of movie experiences, from blockbuster films to independent releases, in state-of-the-art theaters. With multiple locations across different regions, Hollywood Theaters aims to provide audiences with an immersive movie-watching experience and comfortable amenities. Jobs include selling tickets and drinks.", 'Address': 'Rampart Hills View, Colorado Springs, CO 80921', 'Contact': 'Tel: (844) 462-7342 \nEmail: help@hollywoodtheatre.org'},
    {'Name': 'AMC Chapel Hills 13', 'Information': "AMC Theatres is a renowned cinema chain with locations worldwide, offering a diverse range of movies in modern, comfortable theaters. Known for its innovative amenities such as IMAX, Dolby Cinema, and recliner seating, AMC Theatres aims to provide audiences with an exceptional cinematic experience.", 'Address': '1710 Briargate Blvd, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 362-5392 \nEmail: customerservice@amcplus.com'},
    {'Name': 'Life Time Fitness Lifeguard', 'Information': "Lifetime Fitness is a premier health and wellness company that operates luxurious fitness centers offering a wide range of amenities, including state-of-the-art equipment, group fitness classes, spa services, and recreational activities. With a focus on holistic well-being, Lifetime Fitness aims to empower members to achieve their fitness goals and lead healthier lifestyles in a welcoming and supportive environment.", 'Address': '4410 Royal Pine Dr, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 266-9900 \nEmail: help@lifetimefitness.com'},
    {'Name': 'Costco', 'Information': "Costco is a membership-based warehouse club known for offering a wide range of products at discounted prices, including groceries, electronics, home goods, and more. With a focus on bulk purchasing, quality products, and excellent customer service, Costco has become a popular destination for consumers looking to save money while shopping for a variety of items.", 'Address': '5050 N Nevada Ave. Colorado Springs, CO 80909', 'Contact': 'Tel: (719) 264-5010'},
    {'Name': 'King Soopers', 'Information': "King Soopers is a supermarket chain that offers a diverse selection of groceries, household items, and pharmacy services in convenient locations across several states. With a commitment to quality products, competitive pricing, and customer satisfaction, King Soopers aims to meet the needs of shoppers seeking a one-stop destination for their everyday essentials.", 'Address': '9225 N Union Blvd, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 522-2200 \nEmail: customerservice@kroger.com'},
    {'Name': 'Target', 'Information': "Target is a retail chain known for its wide range of products, including clothing, electronics, home goods, and groceries, offered at competitive prices. With a focus on convenience and a pleasant shopping experience, Target stores often feature amenities like in-store cafes, curated displays, and online ordering with same-day pickup or delivery options.", 'Address': '5240 N Academy Blvd Colorado Springs, CO 80918', 'Contact': 'Tel: (719) 594-9600 \nEmail: press@target.com'},
    {'Name': 'Walmart', 'Information': "Walmart is a multinational retail corporation known for its extensive range of products, including groceries, electronics, clothing, and household items, at affordable prices. With a vast network of stores globally and an emphasis on convenience, Walmart offers customers a one-stop shopping destination both in-store and online.", 'Address': '8250 Razorback Rd, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 593-2300 \nEmail: service@walmartcontacts.com'},
    {'Name': 'Barnes & Noble', 'Information': "Barnes & Noble is a well-known retail bookstore chain offering a wide selection of books, magazines, and digital content. With its comfortable reading spaces, cafes, and regular author events, Barnes & Noble provides a welcoming environment for book lovers to explore and enjoy literary culture.", 'Address': '1565 Briargate Blvd, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 266-9960 \nEmail: bninc@bn.com'},
    {'Name': 'Best Buy', 'Information': "Best Buy is a leading electronics retailer known for its extensive selection of technology products, including computers, TVs, smartphones, and home appliances. With a focus on providing expert advice, competitive pricing, and convenient shopping experiences both in-store and online, Best Buy has become a go-to destination for consumers seeking the latest gadgets and electronics.", 'Address': '7675 N Academy Blvd, Colorado Springs, CO 80920', 'Contact': 'Tel: (719) 593 0414 \nEmail: publicrelations@bestbuy.com'},
]


Other = [
    {'Name': 'Scholarship Foundation', 'Information': "Sponsors scholarships, engages in curriculum development, and provides resources for STEM education.", 'Address': '3456 Interquest Pkwy Colorado Springs, CO 80921', 'Contact': 'Tel: (719) 355-9381 \nEmail: help@scholarshipfoundation.org'},
    {'Name': 'Green Earth Co.', 'Information': 'Helps students learn about the envionrment. Promotes healthy choices.', 'Address': '534 Chapel Hills Blvd, Colorado Springs, Colorado 80920', 'Contact': 'Tel: (719) 438-8740 \nEmail: help@greenearth.org'},
    {'Name': 'Water-Smart Co.', 'Information': 'Teaches students about environment, focuses on water, smart choices for environment', 'Address': '7940 Johnson Academy, Colorado Springs, Colorado 80909', 'Contact': 'Tel: (719) 274-6893 \nEmail: customerservice@watersmart.org'},
    {'Name': '21C', 'Information': 'Public Library that provides students with free online reading accounts, provides learning related challenges and games', 'Address': '9284 Chapel Hills Dr. Colorado Springs, Colorado', 'Contact': 'Tel: (719) 574-9835 \nEmail: support@21c.org'},
    {'Name': 'Nutrition Nerd', 'Information': 'Teaches students about the importance of nutrition, fueling, etc', 'Address': '599 Together Lane, Boulder, Colorado', 'Contact': 'Tel: (719) 920-9856 \nEmail: support@nutritionnerd.org'},
    {'Name': 'FireSafe', 'Information': 'Teaches students what to do during different types of fires, proctor fire drills', 'Address': '999 Smokey Lane, Fort Collins, Colorado', 'Contact': 'Tel: (719) 021-9365 \nEmail: help@firesafe.com'},
    {'Name': 'Online Safety Together', 'Information': 'Teaches students about the dangers on online, digital footprints, search history, etc...', 'Address': '7922 Denver Academy Blvd, Denver, Colorado', 'Contact': 'Tel: (719) 025-8655 \nEmail: publicrelations@onlifesafety.com'},
    {'Name': 'Atheltes Joined', 'Information': 'Teaches students about athletics and grades, helping student athletes succeed', 'Address': '89221 Health Blvd, Pueblo, Colorado', 'Contact': 'Tel: (719) 222-7896 \nEmail: support@athletesjoined.org'},
    {'Name': 'Real Life', 'Information': 'Offers real life situations and experiences for students, great for college applications and getting experience', 'Address': '8291 Cascade Blvd, Greely, Colorado', 'Contact': 'Tel: (719) 029-8889 \nEmail: customerservice@reallife.org'},
    {'Name': 'Here2Help', 'Information': 'Helps students with anything they need, provides mentors, tutors, guidance, etc', 'Address': '8111 Cascade Blvd, Colorado Springs, Colorado', 'Contact': 'Tel: (719) 396-9372 \nEmail: help@anything.org'},
    {'Name': 'Admission Help', 'Information': 'Helps students with admissions, gives tips on what to write during essays, offers mentors, provides activities for students to participate in', 'Address': '18990 N Academy Blvd. Colorado Springs, Colorado', 'Contact': 'Tel: (719) 189-6839 \nEmail: support@admissionshelp.org'},
]




#NewAdd = [
    #{'Name': 'New Add', 'Information': '...', 'Address': '...', 'Contact': '(***) *******'},
#]
