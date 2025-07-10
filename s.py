<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bilora License Generator</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --gray-10: #fafafa;
            --gray-50: #f5f7fa;
            --gray-100: #e4e7eb;
            --gray-200: #cbd2d9;
            --gray-300: #9aa5b1;
            --gray-400: #7b8794;
            --gray-500: #616e7c;
            --gray-600: #52606d;
            --gray-700: #3e4c59;
            --gray-800: #323f4b;
            --gray-900: #1f2933;
            --accent: #4b5563;
            --accent-hover: #374151;
            --border: #d1d5db;
            --success: #10b981;
            --warning: #f59e0b;
            --error: #ef4444;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, var(--gray-50), var(--gray-100));
            color: var(--gray-900);
            min-height: 100vh;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            line-height: 1.6;
        }
        
        .container {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
            width: 100%;
            max-width: 520px;
            overflow: hidden;
        }
        
        .header {
            background: var(--gray-800);
            padding: 28px 40px;
            color: white;
            display: flex;
            align-items: center;
            gap: 18px;
        }
        
        .logo-container {
            background: var(--gray-700);
            border-radius: 10px;
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .logo {
            font-size: 28px;
            font-weight: 700;
            color: white;
        }
        
        .header-content {
            flex: 1;
        }
        
        .header h1 {
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 4px;
            letter-spacing: 0.5px;
        }
        
        .header p {
            font-size: 15px;
            color: var(--gray-200);
            opacity: 0.9;
        }
        
        .content {
            padding: 40px;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 24px;
            color: var(--gray-800);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .section-title i {
            color: var(--gray-600);
        }
        
        .form-group {
            margin-bottom: 24px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: var(--gray-700);
            font-size: 15px;
        }
        
        input[type="email"] {
            width: 100%;
            padding: 14px 16px;
            border: 1px solid var(--border);
            border-radius: 8px;
            font-size: 16px;
            transition: all 0.3s ease;
            background: var(--gray-10);
            color: var(--gray-800);
        }
        
        input[type="email"]:focus {
            border-color: var(--gray-500);
            outline: none;
            box-shadow: 0 0 0 3px rgba(107, 114, 128, 0.1);
        }
        
        .policy-notice {
            background-color: rgba(245, 158, 11, 0.08);
            border-left: 4px solid var(--warning);
            padding: 14px;
            border-radius: 0 8px 8px 0;
            margin: 20px 0;
            font-size: 14px;
            color: var(--gray-700);
        }
        
        .policy-notice i {
            color: var(--warning);
            margin-right: 8px;
        }
        
        button {
            background: var(--gray-800);
            color: white;
            border: none;
            padding: 15px 25px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            font-weight: 500;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        
        button:hover {
            background: var(--gray-900);
            transform: translateY(-2px);
        }
        
        .result-container {
            margin-top: 30px;
            border-radius: 10px;
            background: var(--gray-50);
            border-left: 4px solid var(--gray-600);
            padding: 24px;
            display: none;
        }
        
        .result-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 18px;
            padding-bottom: 12px;
            border-bottom: 1px solid var(--gray-100);
        }
        
        .result-title {
            font-weight: 600;
            color: var(--gray-800);
            font-size: 18px;
        }
        
        .license-code {
            font-size: 24px;
            font-weight: 700;
            color: var(--gray-900);
            letter-spacing: 1.5px;
            text-align: center;
            padding: 18px;
            background: white;
            border-radius: 8px;
            margin: 15px 0;
            border: 1px dashed var(--gray-300);
            font-family: monospace;
        }
        
        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-top: 20px;
        }
        
        .info-item {
            background: white;
            padding: 16px;
            border-radius: 8px;
            border: 1px solid var(--gray-100);
        }
        
        .info-label {
            font-size: 13px;
            color: var(--gray-500);
            margin-bottom: 5px;
        }
        
        .info-value {
            font-weight: 500;
            color: var(--gray-800);
            font-size: 15px;
        }
        
        .error {
            color: var(--error);
            background-color: rgba(239, 68, 68, 0.05);
            border: 1px solid rgba(239, 68, 68, 0.2);
            padding: 14px;
            border-radius: 8px;
            margin-top: 20px;
            display: none;
            font-size: 14.5px;
        }
        
        .footer {
            margin-top: 30px;
            padding-top: 25px;
            border-top: 1px solid var(--gray-100);
            text-align: center;
            color: var(--gray-500);
            font-size: 13.5px;
        }
        
        .copyright {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            margin-top: 8px;
        }
        
        .neurospark {
            font-weight: 600;
            color: var(--gray-700);
        }
        
        @media (max-width: 576px) {
            .header {
                padding: 22px;
            }
            
            .content {
                padding: 30px 22px;
            }
            
            .info-grid {
                grid-template-columns: 1fr;
            }
            
            .license-code {
                font-size: 20px;
                padding: 14px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo-container">
                <div class="logo">B</div>
            </div>
            <div class="header-content">
                <h1>Bilora License Generator</h1>
                <p>Secure software licensing system</p>
            </div>
        </div>
        
        <div class="content">
            <div class="section-title">
                <i class="fas fa-key"></i>
                <span>Generate License Code</span>
            </div>
            
            <form id="licenseForm">
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" required placeholder="your.email@company.com">
                </div>
                
                <div class="policy-notice">
                    <i class="fas fa-info-circle"></i>
                    <span>You can generate only one license per month per email address</span>
                </div>
                
                <button type="submit">
                    <i class="fas fa-lock"></i>
                    Generate License
                </button>
            </form>
            
            <div class="error" id="errorMessage"></div>
            
            <div class="result-container" id="resultContainer">
                <div class="result-header">
                    <div class="result-title">License Generated</div>
                    <div><i class="fas fa-check-circle" style="color: var(--success);"></i></div>
                </div>
                
                <div class="license-code" id="licenseCode">A3B5C7D9E1</div>
                
                <div class="info-grid">
                    <div class="info-item">
                        <div class="info-label">Email</div>
                        <div class="info-value" id="userEmail">user@example.com</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">Generated On</div>
                        <div class="info-value" id="generatedDate">2025-07-11</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">Valid Until</div>
                        <div class="info-value" id="expirationDate">2025-07-31</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">Monthly Usage</div>
                        <div class="info-value">1/1</div>
                    </div>
                </div>
            </div>
            
            <div class="footer">
                <p>Secure licensing system for Bilora applications</p>
                <div class="copyright">
                    <span>Made by</span>
                    <span class="neurospark">NeuroSpark Studio</span>
                    <span>• All rights reserved 2025</span>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('licenseForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            // Reset messages
            document.getElementById('errorMessage').style.display = 'none';
            document.getElementById('resultContainer').style.display = 'none';
            
            const email = document.getElementById('email').value;
            
            // Simple email validation
            if (!email || !email.includes('@')) {
                showError('Please enter a valid email address');
                return;
            }
            
            try {
                const response = await fetch('/license', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: `email=${encodeURIComponent(email)}`
                });
                
                const data = await response.json();
                
                if (!response.ok) {
                    throw new Error(data.error || 'Unknown error occurred');
                }
                
                // Format dates
                const formatDate = (dateStr) => {
                    const date = new Date(dateStr);
                    return date.toLocaleDateString('en-US', { 
                        year: 'numeric', 
                        month: 'long', 
                        day: 'numeric' 
                    });
                };
                
                // Update UI
                document.getElementById('licenseCode').textContent = data.license;
                document.getElementById('userEmail').textContent = data.email;
                document.getElementById('generatedDate').textContent = formatDate(data.generated_on);
                document.getElementById('expirationDate').textContent = formatDate(data.expiration);
                
                // Show result
                document.getElementById('resultContainer').style.display = 'block';
                
                // Scroll to results
                document.getElementById('resultContainer').scrollIntoView({ 
                    behavior: 'smooth', 
                    block: 'nearest'
                });
                
            } catch (error) {
                showError(error.message);
            }
        });
        
        function showError(message) {
            const errorElement = document.getElementById('errorMessage');
            errorElement.textContent = message;
            errorElement.style.display = 'block';
        }
    </script>
</body>
</html>
