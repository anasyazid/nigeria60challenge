/* =========== Variable declarations ================== */
const isTeams = document.querySelectorAll(".is-team");
const teamWrapper = document.querySelector(".team-wrapper");
const teamWrapperInput = document.querySelectorAll(".team-wrapper input");
const choiceElem = document.querySelector('.challenge-choice');
const poemContainer = document.querySelectorAll('.poetry');
const sloganContainer = document.querySelectorAll('.slogan');
const photoContainer = document.querySelectorAll('.photo');
let tabContent = document.querySelector("#tab-content");

/* =========== Check if there are team members for entries ================== */
isTeams.forEach(team => {
    team.addEventListener('change', () => {
        tabContent.style.height = "auto"
        if(team.checked && team.value !== 'yes') {
            teamWrapper.classList.add('hidden');
            teamWrapperInput.forEach(elem => {
                elem.classList.remove('input-0');
            })
        }else{
            teamWrapper.classList.remove('hidden');
            teamWrapperInput.forEach(elem => {
                elem.classList.add('input-0');
            })
        }
    });
});

/* =========== Handle Challenge Choice Toggle ================== */
choiceElem.addEventListener('change', (e) => {
    const choice = e.target.value.toLowerCase();
    //Update wizard height
    tabContent.style.height = "auto"

    if(choice) choiceForm(choice);
});

const choiceForm = (choice) => {
    switch(choice) {
        case 'slogan':
            poemContainer.forEach(elem => {
                elem.classList.add('hidden');
            })

            photoContainer.forEach(elem => {
                elem.classList.add('hidden');
            })

            sloganContainer.forEach(elem => {
                elem.classList.remove('hidden');
            })
            break
        case 'photography':
            poemContainer.forEach(elem => {
                elem.classList.add('hidden');
            })

            photoContainer.forEach(elem => {
                elem.classList.remove('hidden');
            })

            sloganContainer.forEach(elem => {
                elem.classList.add('hidden');
            })
            break
        case 'poetry':
            poemContainer.forEach(elem => {
                elem.classList.remove('hidden');
            })

            photoContainer.forEach(elem => {
                elem.classList.add('hidden');
            })

            sloganContainer.forEach(elem => {
                elem.classList.add('hidden');
            })
            break
    }
}


/* =========== Add Member ============ */
const addMemberBtn = document.querySelector('#addMemberBtn');
const memberCotantainer = document.querySelector('#member');

addMemberBtn.addEventListener('click', (e) => {
    const members = document.querySelectorAll('.members');
    const nodeIndex = members.length;

    //Update wizard height
    tabContent.style.height = "auto"
    
    memberCotantainer.innerHTML = memberCotantainer.innerHTML + `<div class="mt-4 col-sm-6 member-remove">
        <input placeholder="Member Name" type="text" name="member[]" required="" class="members input-0"/>
        <span onclick="removeNode(this)"><i class="lni-circle-minus"></i></span>
    </div>`;


})

const removeNode = (elem) => {
    elem.parentNode.remove();
}
