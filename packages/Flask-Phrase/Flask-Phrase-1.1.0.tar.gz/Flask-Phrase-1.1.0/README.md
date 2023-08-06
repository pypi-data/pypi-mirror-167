# Flask-Phrase

This adapter lets you connect your [Flask](http://flask.pocoo.org/) application to [Phrase](https://phrase.com) and integrate the powerful [In-Context-Editor](http://demo.phraseapp.com/) into your apps.

## How does it work?

Flask-Phrase provides In-Context translating facilities to your Flask app by hooking into [Flask-Babel's](https://pythonhosted.org/Flask-Babel/) gettext function. It exposes the underlying key names to the JavaScript editor that is provided by Phrase.

To get started with Phrase you need to [sign up for a free account](https://phrase.com/signup).

## Install and Setup

Install the package with pip:

    pip install Flask-Phrase


Add the following to your Flask app configuration (app.config or config.py file)

    PHRASEAPP_ENABLED = True
    PHRASEAPP_PREFIX = '{{__'
    PHRASEAPP_SUFFIX = '__}}'

Your app code should look something like this:

    from flask import Flask, [...]
    from flask.ext.babel import Babel
    from flask_phrase import Phrase, gettext, ngettext
    app = Flask(__name__)
    babel = Babel(app)
    phrase = Phrase(app)

Last step: add the Phrase JavaScript snippet to your base layout file with the folling tag. This should go inside the <head> section of your template file:

    <script>
    window.PHRASEAPP_CONFIG = {
        projectId: "YOUR-PROJECT-ID"
    };
    (function() {
        var phraseapp = document.createElement('script'); phraseapp.type = 'text/javascript'; phraseapp.async = true;
        phraseapp.src = ['https://', 'phraseapp.com/assets/in-context-editor/2.0/app.js?', new Date().getTime()].join('');
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(phraseapp, s);
    })();
    </script>

You can find your Project-ID in the Phrase Translation Center.


## Using the US Datacenter with ICE

In addition to `projectId` in the config, also add the US specific URLs to enable working through the US endpoint.
```
    baseUrl: "https://us.app.phrase.com",
    apiBaseUrl: 'https://api.us.app.phrase.com/api/v2',
    oauthEndpointUrl: "https://api.us.app.phrase.com/api/v2/authorizations",
    profileUrl: "https://us.app.phrase.com/settings/profile",
```

e.g
```
window.PHRASEAPP_CONFIG = {
    projectId: "YOUR-PROJECT-ID",
    baseUrl: "https://us.app.phrase.com",
    apiBaseUrl: 'https://api.us.app.phrase.com/api/v2',
    oauthEndpointUrl: "https://api.us.app.phrase.com/api/v2/authorizations",
    profileUrl: "https://us.app.phrase.com/settings/profile",
};
```

## Usage

Set the PHRASEAPP_ENABLED to True/False to enable or disable In-Context-Editing. When set to False, it will fall back to standard Flask-Babel's gettext functions. Disable Phrase for production environments at any time!

## Resources
* [Step-by-Step Guide on Flask-Babel and Flask-Phrase](https://phrase.com/blog/posts/python-localization-for-flask-applications/)
* [Flask-Phrase Demo Application](https://github.com/phrase/flask-demo-application/).
* [Localization Guides and Software Translation Best Practices](http://phrase.com/blog/)
* [Contact Phrase Team](https://phrase.com/en/contact)

## Get help / support

Please contact [support@phrase.com](mailto:support@phrase.com?subject=[GitHub]%20) and we can take more direct action toward finding a solution.
