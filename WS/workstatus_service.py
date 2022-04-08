from flask import Flask, jsonify
import BAL.workstatus

def workstatus_service():

    app = Flask(__name__)
    app.config["DEBUG"] = True

    @app.route('/v1/stats/data/full', methods=['GET'])
    def get_full_dataset():
        return jsonify(BAL.workstatus.get_full_dataset())


    @app.route('/v1/stats/data/students', methods=['GET'])
    def get_students_data():
        return jsonify(BAL.workstatus.get_students_data())

    @app.route('/v1/stats/data/province/<province>', methods=['GET'])
    def get_data_per_province(province):
        return jsonify(BAL.workstatus.get_province_data(province))

    @app.route('/v1/stats/data/lfs/<code>', methods=['GET'])
    def get_data_per_lfs_code(code):
        return jsonify(BAL.workstatus.get_data_per_lfs_code(code))

    @app.route('/', methods=['GET'])
    def home():
        return """<h1>Sales Statistics</h1><p>This site is a prototype API for reporting sales
           statistics for use with Python and Pandas clients.</p>"""

    app.run(host='0.0.0.0')