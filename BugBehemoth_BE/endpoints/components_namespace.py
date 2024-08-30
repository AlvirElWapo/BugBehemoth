from flask import Blueprint, render_template_string

modals_bp = Blueprint('modals_bp', __name__)

@modals_bp.route('/login-form')
def login_form():
    return render_template_string('''
    <!-- LOGIN FORM -->
    <div id="login-form">
      <!-- EMAIL/USERNAME -->
      <label class="input input-bordered flex items-center gap-5 mb-5">
        <i class="fa-regular fa-envelope"></i>
        <input type="text" class="grow" placeholder="Email/Username" />
      </label>
      <!-- PASSWORD -->
      <label class="input input-bordered flex items-center gap-5 mb-2 justify-self-end">
        <input type="password" class="grow" placeholder="Password" />
      </label>
    </div>
    ''')

@modals_bp.route('/register-form')
def register_form():
    return render_template_string('''
    <!-- REGISTER FORM -->
    <div id="register-form">
      <!-- USERNAME -->
      <label class="input input-bordered flex items-center gap-5 mb-5">
        <i class="fa-solid fa-user"></i>
        <input type="text" class="grow" placeholder="Username" />
      </label>
      <!-- EMAIL -->
      <label class="input input-bordered flex items-center gap-5 mb-5">
        <i class="fa-regular fa-envelope"></i>
        <input type="text" class="grow" placeholder="Email" />
      </label>
      <!-- PASSWORD -->
      <label class="input input-bordered flex items-center gap-5 mb-2 justify-self-end">
        <input type="password" class="grow" placeholder="Password" />
      </label>
      <!-- CONFIRM PASSWORD -->
      <label class="input input-bordered flex items-center gap-5 mb-2 justify-self-end">
        <input type="password" class="grow" placeholder="Confirm Password" />
      </label>
    </div>
    ''')
