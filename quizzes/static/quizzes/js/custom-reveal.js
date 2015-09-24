document.addEventListener( 'keydown', onDocumentKeyDown, false );

answers = [];
result_saved = false;

/**
 * Handler for the document level 'keydown' event.
 */
 function onDocumentKeyDown( event ) {
    //console.log("Key: "+event.keyCode)
    
    //When the quiz has ended, shos results
    var progress = Reveal.getProgress(); // 0-1
    //console.log("Progress is: "+progress);
    if (progress === 1 && !result_saved) {
        var sum = _.reduce(answers, function(memo, num){ return memo + num; }, 0);
        var score = sum*100/answers.length;
        var deck_name = $(".slides").attr("data-deck-name")
        //console.log("This is the end! Score: "+score+" for: "+deck_name);

        //Hide slides
        $(".reveal").hide()
        //Show results
        $("#score").text(score)
        $("#result").show()
        //Send a POST request
        $.post("/quizzes/save/",
        {
            name: deck_name,
            score: score
        },
            function(data, status){
            console.log("This is the end! Score: "+score+" for: "+deck_name);
            console.log("Data: " + data + "\nStatus: " + status);
            result_saved = true;
        });
    };

    // Check if there's a focused element that could be using
    // the keyboard
    var activeElementIsCE = document.activeElement && document.activeElement.contentEditable !== 'inherit';
    var activeElementIsInput = document.activeElement && document.activeElement.tagName && /input|textarea/i.test( document.activeElement.tagName );

    // Disregard the event if there's a focused element or a
    // keyboard modifier key is present
    if( activeElementIsCE || activeElementIsInput || (event.shiftKey && event.keyCode !== 32) || event.altKey || event.ctrlKey || event.metaKey ) return;

    //Check if current slide is question or answer
    var card_type = Reveal.getCurrentSlide().getAttribute('data-type');
    //console.log('Card is '+card_type);
    //Question allows only enter key
    //Answers allows only T or F key

    var triggered = false;

    // 2. System defined key bindings
    if( triggered === false ) {

        // Assume true and try to prove false
        triggered = true;

        //is question and pressed Enter key
        if (card_type==='question'){
            if(event.keyCode===13) Reveal.down();
            else console.log('Only Enter allowed')
        //is answer
        }else if(card_type==='answer'){
            //Pressed T
            if(event.keyCode==84){
                answers.push(1);
                Reveal.right();
            //Pressed F
            }else if(event.keyCode==70){
                answers.push(0);
                Reveal.right();

            }else{
                triggered = false;
                console.log('Only T or F allowed')
            }
        }else{
            triggered = false;
            console.log('Unkwown card type')
        };

    }

    // If the input resulted in a triggered action we should prevent
    // the browsers default behavior
    if( triggered ) {
        event.preventDefault && event.preventDefault();
    }
    // ESC or O key
    else if ( ( event.keyCode === 27 || event.keyCode === 79 ) && features.transforms3d ) {
        if( dom.overlay ) {
            closeOverlay();
        }
        else {
            toggleOverview();
        }

        event.preventDefault && event.preventDefault();
    }
}