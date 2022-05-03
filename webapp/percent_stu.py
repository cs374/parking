from datetime import date
from flask import Flask, render_template, request, flash, redirect
import psycopg, re, app, datetime

def percent_stu_combo():
    return render_template('percent_stu.html')