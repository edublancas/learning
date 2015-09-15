document.addEventListener( 'keydown', onDocumentKeyDown, false );

answers = []

/**
 * Handler for the document level 'keydown' event.
 */
 function onDocumentKeyDown( event ) {
    //console.log("Key: "+event.keyCode)
    
    //When the quiz has ended, shos results
    var progress = Reveal.getProgress(); // 0-1
    console.log("Progress is: "+progress);
    if (progress === 1) {
        var sum = _.reduce(answers, function(memo, num){ return memo + num; }, 0);
        var score = sum*100/answers.length;
        console.log("This is the end! Score: "+score);

        //Hide slides
        $(".reveal").hide()
        //Show results
        $("#score").text(score)
        $("#result").show()
        //Save row to db
    };

    // Check if there's a focused element that could be using
    // the keyboard
    var activeElementIsCE = document.activeElement && document.activeElement.contentEditable !== 'inherit';
    var activeElementIsInput = document.activeElement && document.activeElement.tagName && /input|textarea/i.test( document.activeElement.tagName );

    // Disregard the event if there's a focused element or a
    // keyboard modifier key is present
    if( activeElementIsCE || activeElementIsInput || (event.shiftKey && event.keyCode !== 32) || event.altKey || event.ctrlKey || event.metaKey ) return;


    var triggered = false;

    // 2. System defined key bindings
    if( triggered === false ) {

        // Assume true and try to prove false
        triggered = true;

        switch( event.keyCode ) {
            // Enter
            case 13: 
                Reveal.down();
                break;
            // T (correct answer)
            case 84:
                answers.push(1);
                Reveal.right();
                break;
            // F (incorrect answer)
            case 70:
                Reveal.right();
                answers.push(0);
                break;
            default: triggered = false;
        }

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