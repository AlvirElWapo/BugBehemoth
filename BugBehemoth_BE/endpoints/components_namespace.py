from flask import Blueprint, render_template_string

modals_bp = Blueprint('modals_bp', __name__)

@modals_bp.route('/login-form')
def login_form():
    return render_template_string('''
      <form
      hx-post="/auth/login"
      hx-trigger="submit"
      hx-target="#diditwork"
      hx-ext="json-enc"

      >
        <div id="login-form">
          <label for="email_or_user" class="input input-bordered flex items-center gap-5 mb-5">
            <i class="fa-regular fa-envelope"></i>
            <input type="text" id="email" name="email" class="grow" placeholder="Email" />
          </label>
          <label class="input input-bordered flex items-center gap-5 mb-2 justify-self-end">
            <input type="password" id="password" name="password" class="grow" placeholder="Contraseña" />
          </label>
        </div>
        <div class="flex justify-end">
          <button type="submit" class="btn btn-primary">
            Ingresar 
          </button>
        </div>
      </form>
    ''')

@modals_bp.route('/register-form')
def register_form():
    return render_template_string('''
      <form
      hx-post="/auth/register"
      hx-trigger="submit"
      hx-target="#diditwork"
      hx-ext="json-enc"

      >
    <!-- REGISTER FORM -->
    <div id="register-form">
      <!-- EMAIL -->
      <label class="input input-bordered flex items-center gap-5 mb-5">
        <i class="fa-regular fa-envelope"></i>
        <input type="text" id="email" name="email" class="grow" placeholder="Email" />
      </label>
      <!-- PASSWORD -->
      <label class="input input-bordered flex items-center gap-5 mb-2 justify-self-end">
        <input type="password" id="email" name="password" class="grow" placeholder="Contraseña" />
      </label>
      <div class="flex justify-end">
        <button hx-post="/auth/login" hx-trigger="click" hx-target="#time-display" class="btn btn-primary">
        Registrarse 
        </button>
      </div>
    </div>
    </form>
    ''')
