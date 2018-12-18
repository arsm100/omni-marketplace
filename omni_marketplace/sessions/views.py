from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, escape, sessions


sessions_blueprint = Blueprint(
    'sessions', __name__, template_folder='templates/')
