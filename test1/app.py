from flask import Flask, render_template, request
import logging

app = Flask(__name__)
# make sure Flask’s logger will show DEBUG messages
app.logger.setLevel(logging.DEBUG)

def advice_calculator(appliance: str) -> str:
    """
    Stub for water‐saving advice.
    Takes the appliance name as input and returns a suggestion.
    """
    # nothing here yet, so we immediately return an empty string
    return ""

@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.debug("Index page hit, method=%s", request.method)
    water_saving_measure = None

    if request.method == 'POST':
        # 1) grab the form data
        appliance = request.form.get('appliance', None)
        app.logger.debug("Received appliance: %r", appliance)

        # 2) make sure we actually got something
        if appliance is None:
            app.logger.warning("No appliance field in form!")
            # fail fast: re-render immediately rather than hanging
            return render_template('index.html', water_saving_measure="Error: no input")

        # 3) compute (this should return immediately)
        water_saving_measure = advice_calculator(appliance)
        app.logger.debug("Advice is ready, returning template")

        # 4) return the rendered template
        return render_template('index.html',
                               water_saving_measure=water_saving_measure)

    # GET always returns
    return render_template('index.html',
                           water_saving_measure=None)

if __name__ == '__main__':
    app.run(debug=True)
