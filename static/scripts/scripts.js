$(document).ready(function() {
    // Handle the form submission
    $('#chat_form').on('submit', function(e) {
        e.preventDefault();
        
        // Get the user's input
        var userInput = $('#user_input').val();
        
        if (userInput.trim() !== "") {
            // Display the user's question in the chatbox
            $('#chatbox').append('<div><b>You:</b> ' + userInput + '</div>');
            
            // Show the "Bot is typing..." message
            $('#bot_typing').show();

            // Send the input to the server (Flask)
            $.ajax({
                url: '/ask',
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ question: userInput }),  // Sending the user's question
                success: function(response) {
                    $('#bot_typing').hide();
                    $('#chatbox').append('<div><b>Bot:</b> ' + response.answer + '</div>');
                    $('#chatbox').scrollTop($('#chatbox')[0].scrollHeight);
                },
                error: function() {
                    $('#bot_typing').hide();
                    $('#chatbox').append('<div><b>Bot:</b> Sorry, I could not understand the question.</div>');
                }
            });
        }

        // Clear the input field
        $('#user_input').val('');
    });
});
