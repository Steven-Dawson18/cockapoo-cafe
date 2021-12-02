function sendMail(contactForm) {
    var templateParams = {
        from_email: contactForm.emailaddress.value,
        message: contactForm.message.value,
        from_name: contactForm.name.value
    };

    emailjs.send('service_evux4oc', 'cafe', templateParams)

        .then(function(response) {
        console.log('SUCCESS!', response.status, response.text);
        }, function(error) {
        console.log('FAILED...', error);
        });
        return false;
}