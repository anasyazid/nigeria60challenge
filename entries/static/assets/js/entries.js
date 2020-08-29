/* =========== Handle Challenge Choice Toggle ================== */
const choiceElem = document.querySelector('.challenge-choice');
const poemContainer = document.querySelectorAll('.poetry');
const sloganContainer = document.querySelectorAll('.slogan');
const photoContainer = document.querySelectorAll('.photo');

choiceElem.addEventListener('change', (e) => {
    const choice = e.target.value.toLowerCase();
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
    
    memberCotantainer.innerHTML = memberCotantainer.innerHTML + `<div class="mt-4 col-sm-6 member-remove">
        <input placeholder="Member Name" type="text" name="member[]" required="" class="members input-0"/>
        <span onclick="removeNode(this)"><i class="lni-circle-minus"></i></span>
    </div>`;


})

const removeNode = (elem) => {
    elem.parentNode.remove();
}