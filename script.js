let Title =[
    
    
    "054-4377422",
    "Yuvalkashi1@gmail.com",
    "Central Israel (Rishon Le-Zion) & beer sheva",
    "<a target=\"_blank\" href=\"https://www.linkedin.com/in/yuval-kashi/\"> Linkdin </a>"
    
];

const Expo = [
    {
	    lines: ["Computer Science student, Third year, 2 more semesters. 8200 alumni. GPA 83.5, PET* 720.",
                "Pre university I worked at a software company as an analyst,",
                "I am used to teamwork, attention to details and have organizational skills,",
                "used to speak with foreign team members in English and Absolutely confident!",
                " I look for a Software developer position part-time / intern / fulltime"
            ]
    }
    ];


const Education = [
    {
        place: "B.Sc. Computer Science \55 Ben-Gurion University, Beer Sheva",
        years: "(2018 \55 present)",
	    lines: ["GPA: 83.5",
                "Psychometric Test Score: 720",
                "Top grades in Architecture and System Programming: 91, Principles of Programming: 88.",
                "Participated at the \"Ashalim\" excellence program at my First year."]
    },
    {   
        place: "Science\55oriented studies \55 High School",
        years: "(2010 \55 2013)",
        lines: ["Full high school diploma with honor. GPA: 114.",
                "5 units of Computer science, English, Math and chemistry."]

    }];
	
const Projects = [
    {
        name: "Mission organizer program \55 MI6 agency",
        lang: ["Java with multithreading"],
	    lines: ["Developed a system that assigns missions to agents in secret service agency.",
                "Implementing diverse concurrency design patterns such as singleton, call-backs and Synchronization Patterns."]
    },
    {
        name: "Streaming Service System",
        lang: ["C++"],
	    lines: ["Used several design patterns such as the Visitor and Double dispatch and Factory.",
                "Designed an object-oriented system in C++ using the “Rule of 5” including memory management."]
    },
    {
        name: "Web scraper for easy Stocks data getter",
        lang: ["Python"],
	    lines: ["Created a script that generates excel sheets with preferred stocks data by using python packages."]
    },
    {
        name: "Resume website",
        lang: ["Java Script", "HTML", "CSS"],
	    lines: ["Resume website designed with passion to make another interactive way to check out my skills."]
    }];




function lines(lines){ 
   return `<h4>
        <ul class = "content">
            ${lines.map( line => `<li>${line}</li>` ).join('')}
        </ul>
    </h4>`
}

function parse_edu(item) {
    return `<div class="bullet-in">
            <h2 class="place"> ${item.place} </h2>
            <h3 class="years"> ${item.years} </h3>
            <h3 class="lines"> ${ item.lines ? lines(item.lines) : '' } </h3>
            </div>
            `
}

function parse_projects(item) {
    return `<div class="bullet-in">
            <h2 class="name"> ${item.name} </h2>
            <h3 class="lang"> ${item.lang} </h3>
            <h3 class="lines"> ${ item.lines ? lines(item.lines) : '' } </h3>
            </div>
            `
}

// notice that the achievements href cannot be 2 words with &
function page_nav() {

    let sections = ["Quick View", "Education", "Projects", "Photos", "Achievements\40\46\40diplomas"]
    return `<div class = "page-nav">
                ${sections.map(str => `<a href=#${str}><div class = "nav-link-wrapper">${str}</div></a>`).join(' ')}
            </div>`
}

function return_button() {
    return `<a href="#name"><div class = "nav-link-wrapper-ret">return</div></a>`
    
}

{/* <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
  <path fill="#0099ff" fill-opacity="1" d="M0,192L48,176C96,160,192,128,288,112C384,96,480,96,576,128C672,160,768,224,864,250.7C960,277,1056,267,1152,229.3C1248,192,1344,128,1392,96L1440,64L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
</svg> */}

// 0099ff

document.getElementById("test").innerHTML = `    

    <div class="welcomer">
        <div class="nav">
        <h1 id="name"> Yuval Kashi </h1>
        ${page_nav()}
        </div>
        
        <div class="welcomer_content">
        <h3 class="title"> ${lines(Title)} </h3>
        </div>
        
        <svg class="wave" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="#fff" fill-opacity="1" d="M0,32L80,26.7C160,21,320,11,480,37.3C640,64,800,128,960,133.3C1120,139,1280,85,1360,58.7L1440,32L1440,320L1360,320C1280,320,1120,320,960,320C800,320,640,320,480,320C320,320,160,320,80,320L0,320Z"></path></svg>
    </div>

    <div class="real_body">
        
        
        <h1 class="bullet" id="Quick"> Quick View </h1>
        <div class="bullet-in"> ${lines(Expo[0].lines)} </div>
        ${return_button()}

        <h1 class="bullet" id="Education"> Education (${Education.length} milestones)</h1>
        ${Education.map(parse_edu).join('')}
        ${return_button()}
        
        <h1 class="bullet" id="Projects"> Projects (${Projects.length} worth mentioning)</h1>
        ${Projects.map(parse_projects).join('')}
        ${return_button()}
        
        <h1 class="bullet" id="Photos"> Photos </h1>
        ${return_button()}
        

        
        <h1 class="bullet" id="Achievements"> Achievements & diplomas </h1>
        
        ${return_button()}

        <footer>Yuval Kashi</footer>
    </div>

`