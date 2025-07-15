# Claude Code Official Documentation

*Last updated: 2025-07-15 15:35 UTC*
*Source: https://docs.anthropic.com/en/docs/claude-code*

---

:root {
--primary: 14 14 14;
--primary-light: 212 162 127;
--primary-dark: 14 14 14;
--background-light: 253 253 247;
--background-dark: 9 9 11;
--gray-50: 243 243 243;
--gray-100: 238 238 238;
--gray-200: 222 222 222;
--gray-300: 206 206 206;
--gray-400: 158 158 158;
--gray-500: 112 112 112;
--gray-600: 80 80 80;
--gray-700: 62 62 62;
--gray-800: 37 37 37;
--gray-900: 23 23 23;
--gray-950: 10 10 10;
}@font-face {
font-family: "Styrene Display";
src: url("https://www-cdn.anthropic.com/e8f9c8ca51b03efb6315db351446fc972ab15abe/StyreneA-Medium-Web.woff2")
format("woff2");
font-weight: 500;
font-style: normal;
font-stretch: normal;
}
@font-face {
font-family: "Styrene Display";
src: url("https://www-cdn.anthropic.com/e8f9c8ca51b03efb6315db351446fc972ab15abe/StyreneA-Medium-Web.woff2")
format("woff2");
font-weight: 600;
font-style: normal;
font-stretch: normal;
}
@font-face {
font-family: "Styrene";
src: url("https://www-cdn.anthropic.com/6f87b6d99aefde021ac24f21295bf9e70f71472f/StyreneBLC-Regular.woff2")
format("woff2");
font-weight: 400;
font-style: normal;
font-stretch: normal;
}
@font-face {
font-family: "Styrene";
src: url("https://www-cdn.anthropic.com/6f87b6d99aefde021ac24f21295bf9e70f71472f/StyreneBLC-Regular.woff2")
format("woff2");
font-weight: 500;
font-style: normal;
font-stretch: normal;
}
@font-face {
font-family: "Styrene";
src: url("https://www-cdn.anthropic.com/3611e9e4aaaf466dbd47e2686f561e7de694cb6c/StyreneBLC-Medium.woff2")
format("woff2");
font-weight: 600;
font-style: normal;
font-stretch: normal;
}
@font-face {
font-family: "Tiempos";
src: url("https://www-cdn.anthropic.com/c3e09cefbfeb4e5eaca56b7bc8b9a1aa1aeda025/TiemposText-Regular.woff2")
format("woff2");
font-weight: 400;
font-style: normal;
font-stretch: normal;
}
@font-face {
font-family: "Tiempos";
src: url("https://www-cdn.anthropic.com/b198ca4e31a323b2abb84b3eeeb1eed1f471afa0/TiemposText-Medium.woff2")
format("woff2");
font-weight: 500;
font-style: normal;
font-stretch: normal;
}
@font-face {
font-family: "Tiempos";
src: url("https://www-cdn.anthropic.com/b198ca4e31a323b2abb84b3eeeb1eed1f471afa0/TiemposText-Medium.woff2")
format("woff2");
font-weight: 600;
font-style: normal;
font-stretch: normal;
}
@font-face {
font-family: "Copernicus";
src: url("https://www-cdn.anthropic.com/db30aec85c7615f4a4d3e23c0c941674ea67f8f5/Copernicus-Book.woff2")
format("woff2");
font-weight: 300; /\* Assuming 300 is the lightest available weight \*/
font-style: normal;
}
/\* Color variables copied from https://github.com/anthropics/apps/blob/main/packages/ui/themes/generated/theme-colors.css \*/
:root {
--always-white: 0 0% 100%;
--always-black: 0 0% 0%;
--constant-book-cloth: 15 55% 80%;
--constant-clay: 15 60% 85%;
--constant-kraft: 25 40% 83%;
--constant-manilla: 40 20% 92%;
--constant-slate-000: 0 0% 100%;
--constant-slate-050: 48 33.3% 97.1%;
--constant-slate-100: 53 28.6% 94.5%;
--constant-slate-150: 48 25% 92.2%;
--constant-slate-200: 50 20.7% 88.6%;
--constant-slate-250: 51 16.5% 84.5%;
--constant-slate-300: 50 11.5% 79.6%;
--constant-slate-350: 50 9% 73.7%;
--constant-slate-400: 49 6.5% 66.9%;
--constant-slate-450: 48 4.8% 59.2%;
--constant-slate-500: 53 3.2% 51.4%;
--constant-slate-550: 51 3.1% 43.7%;
--constant-slate-600: 48 2.7% 35.9%;
--constant-slate-650: 48 3.4% 29.2%;
--constant-slate-700: 60 2.5% 23.3%;
--constant-slate-750: 60 2.1% 18.4%;
--constant-slate-800: 60 2.7% 14.5%;
--constant-slate-850: 30 3.3% 11.8%;
--constant-slate-900: 30 4% 9.8%;
--constant-slate-950: 60 2.6% 7.6%;
--constant-slate-1000: 60 3.4% 5.7%;
}
:root:not(.dark) {
--accent-brand: 15 63.1% 59.6%;
--accent-main-000: 15 55.6% 52.4%;
--accent-main-100: 15 55.6% 52.4%;
--accent-main-200: 15 63.1% 59.6%;
--accent-main-900: 0 0% 0%;
--accent-pro-000: 251 34.2% 33.3%;
--accent-pro-100: 251 40% 45.1%;
--accent-pro-200: 251 61% 72.2%;
--accent-pro-900: 253 33.3% 91.8%;
--accent-secondary-000: 210 73.7% 40.2%;
--accent-secondary-100: 210 70.9% 51.6%;
--accent-secondary-200: 210 70.9% 51.6%;
--accent-secondary-900: 211 72% 90%;
--bg-000: 0 0% 100%;
--bg-100: 48 33.3% 97.1%;
--bg-200: 53 28.6% 94.5%;
--bg-300: 48 25% 92.2%;
--bg-400: 50 20.7% 88.6%;
--bg-500: 50 20.7% 88.6%;
--border-100: 30 3.3% 11.8%;
--border-200: 30 3.3% 11.8%;
--border-300: 30 3.3% 11.8%;
--border-400: 30 3.3% 11.8%;
--danger-000: 0 61.4% 22.4%;
--danger-100: 0 58.6% 34.1%;
--danger-200: 0 58.6% 34.1%;
--danger-900: 0 50% 95%;
--oncolor-100: 0 0% 100%;
--oncolor-200: 60 6.7% 97.1%;
--oncolor-300: 60 6.7% 97.1%;
--text-000: 60 2.6% 7.6%;
--text-100: 60 2.6% 7.6%;
--text-200: 60 2.5% 23.3%;
--text-300: 60 2.5% 23.3%;
--text-400: 51 3.1% 43.7%;
--text-500: 51 3.1% 43.7%;
}
:root.dark {
--accent-brand: 15 63.1% 59.6%;
--accent-main-000: 15 55.6% 52.4%;
--accent-main-100: 15 63.1% 59.6%;
--accent-main-200: 15 63.1% 59.6%;
--accent-main-900: 0 0% 0%;
--accent-pro-000: 251 84.6% 74.5%;
--accent-pro-100: 251 40.2% 54.1%;
--accent-pro-200: 251 40% 45.1%;
--accent-pro-900: 250 25.3% 19.4%;
--accent-secondary-000: 210 71.1% 62%;
--accent-secondary-100: 210 70.9% 51.6%;
--accent-secondary-200: 210 70.9% 51.6%;
--accent-secondary-900: 210 55.9% 24.6%;
--bg-000: 60 2.1% 18.4%;
--bg-100: 60 2.7% 14.5%;
--bg-200: 30 3.3% 11.8%;
--bg-300: 60 2.6% 7.6%;
--bg-400: 60 3.4% 5.7%;
--bg-500: 60 3.4% 5.7%;
--border-100: 51 16.5% 84.5%;
--border-200: 51 16.5% 84.5%;
--border-300: 51 16.5% 84.5%;
--border-400: 51 16.5% 84.5%;
--danger-000: 0 73.1% 66.5%;
--danger-100: 0 58.6% 34.1%;
--danger-200: 0 58.6% 34.1%;
--danger-900: 0 23% 15.6%;
--oncolor-100: 0 0% 100%;
--oncolor-200: 60 6.7% 97.1%;
--oncolor-300: 60 6.7% 97.1%;
--text-000: 48 33.3% 97.1%;
--text-100: 48 33.3% 97.1%;
--text-200: 50 9% 73.7%;
--text-300: 50 9% 73.7%;
--text-400: 48 4.8% 59.2%;
--text-500: 48 4.8% 59.2%;
}
#home-header {
font-family: "Copernicus", sans-serif;
font-weight: 300 !important;
font-size: 50px;
line-height: 1.2;
margin-bottom: 1rem;
color: --text-000;
display: flex;
align-items: baseline;
justify-content: center;
flex-wrap: nowrap;
}
/\* Responsive layout for the home header - left align on larger screens \*/
@media (min-width: 768px) {
#home-header {
justify-content: flex-start;
}
}
.build-with {
font-family: "Copernicus", sans-serif;
white-space: nowrap;
letter-spacing: -0.02em;
}
.claude-wordmark-wrapper {
display: inline-flex;
align-items: baseline;
margin-left: 10px; /\* Space between "Build with" and the wordmark \*/
}
.claude-wordmark {
height: 40px; /\* Adjust this value to match your desired size \*/
width: auto;
position: relative;
}
.dark #home-header {
color: white;
}
.description-text {
color: black;
}
.dark .description-text {
color: white;
}
.dark .claude-wordmark {
filter: invert(1);
}
:root {
--bg-color: #f0efea;
}
.dark {
--bg-color: #2b2b2b;
}
#background-div {
}
body,
input,
#category-select,
.dropdown-item,
#table-of-contents {
font-family: "Styrene", sans-serif;
}
.eyebrow {
font-family: "Styrene Display", sans-serif;
text-transform: uppercase;
letter-spacing: 0.02rem;
}
#content-container {
font-family: "Tiempos", serif;
}
#content-container h1,
#content-container h2,
#content-container h3,
#content-container h4,
#content-container h5,
#content-container h6 {
font-family: "Styrene Display", sans-serif;
}
#content-container p {
font-size: 1rem;
line-height: 1.65rem;
}
.font-extrabold {
font-weight: 600 !important;
}
.wide-table {
width: 100%;
overflow-x: auto;
}
.wide-table table {
width: 175%;
margin-bottom: 0;
}
/\* Prompt Library \*/
#prompt-library-container {
margin: 4rem auto;
max-width: 48rem;
padding-left: 1.25rem;
padding-right: 1.25rem;
}
.prompt-library-title {
font-size: 24px;
text-align: center;
font-weight: 700;
color: #1f2937;
}
.dark .prompt-library-title {
color: #e5e7eb;
}
.prompt-library-description {
margin-top: 1rem;
text-align: center;
}
.main-content {
margin-bottom: 10rem;
max-width: 64rem;
margin-left: auto;
margin-right: auto;
padding-left: 1.25rem;
padding-right: 1.25rem;
}
.prompt-controllers {
display: flex;
gap: 0.5rem;
}
.prompt-search-container {
position: relative;
flex: 1 1 0%;
}
.prompt-search-icon-container {
display: flex;
position: absolute;
top: 0;
bottom: 0;
left: 0;
align-items: center;
padding-left: 0.75rem;
}
.prompt-search-icon {
margin-left: 0.25rem;
margin-right: 0.75rem;
flex: none;
width: 1rem;
height: 1rem;
background-color: #6b7280;
mask-image: url(https://mintlify.b-cdn.net/v6.5.1/solid/magnifying-glass.svg);
mask-repeat: no-repeat;
mask-position: center center;
}
input.prompt-search-bar {
display: block;
height: 2.5rem;
padding-left: 2.5rem;
border-radius: 0.75rem;
border-width: 1px;
background-color: #ffffff;
width: 100%;
color: #111827;
box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}
.dark input.prompt-search-bar {
color: #ffffff;
background-color: rgb(var(--background-dark));
border-color: #d1d5db1a;
}
input.prompt-search-bar:focus {
outline-color: rgb(var(--primary));
}
.dark input.prompt-search-bar:focus {
outline-color: rgb(var(--primary-light));
}
.dark .prompt-search-icon {
background-color: #ffffff80;
}
#category-select {
padding-left: 1rem;
padding-right: 2.5rem;
height: 2.5rem;
display: flex;
align-items: center;
border-radius: 0.75rem;
border-width: 1px;
color: #111827;
background-color: #ffffff;
cursor: pointer;
box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
white-space: nowrap;
}
.dark #category-select {
background-color: rgb(var(--background-dark));
border-color: #d1d5db1a;
color: #ffffff;
}
#category-select:hover {
background-color: #f9fafb;
}
.dark #category-select:hover {
background-color: #ffffff0d;
}
#category-select:focus {
outline-color: rgb(var(--primary));
}
.dark #category-select:focus {
outline-color: rgb(var(--primary-light));
}
#categories-dropdown {
top: calc(100% + 4px);
padding: 0.5rem 0.5rem;
display: none;
position: absolute;
z-index: 10;
border-radius: 0.75rem;
border-width: 1px;
width: 100%;
color: #111827;
background-color: #ffffff;
box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}
.dark #categories-dropdown {
background-color: rgb(var(--background-dark));
border-color: #d1d5db1a;
color: #ffffff;
}
#categories-dropdown-clickout {
position: fixed;
top: 0;
right: 0;
bottom: 0;
left: 0;
z-index: 0;
}
.dropdown-icon-container {
display: flex;
position: absolute;
top: 0;
bottom: 0;
right: 0;
align-items: center;
padding-right: 0.25rem;
}
.dropdown-icon {
margin-left: 0.25rem;
margin-right: 0.75rem;
flex: none;
width: 0.75rem;
height: 0.75rem;
background-color: #6b7280;
mask-image: url(https://mintlify.b-cdn.net/v6.5.1/solid/caret-down.svg);
mask-repeat: no-repeat;
mask-position: center center;
}
.dark .dropdown-icon {
background-color: #ffffff80;
}
#prompts-container {
grid-template-columns: repeat(1, minmax(0, 1fr));
gap: 2rem;
}
.dropdown-item {
padding: 0.25rem 0.5rem;
border-radius: 0.375rem;
display: flex;
align-items: center;
cursor: pointer;
}
.dropdown-item:hover {
background-color: #f9fafb;
}
.dark .dropdown-item:hover {
background-color: #ffffff0d;
}
.check-icon {
mask-image: url(https://mintlify.b-cdn.net/v6.5.1/solid/check.svg);
height: 0.875rem;
width: 1rem;
background-color: rgb(var(--primary-light));
mask-repeat: no-repeat;
mask-position: center center;
}
.prompt-card {
margin: -0.75rem;
padding: 0.75rem;
display: flex;
border-radius: 1rem;
}
.prompt-card:hover {
background-color: #03071208;
}
.dark .prompt-card:hover {
background-color: #ffffff08;
}
.prompt-icon-container {
display: flex;
flex: none;
align-items: center;
justify-content: center;
margin-right: 1.5rem;
border-radius: 0.75rem;
height: 4rem;
width: 4rem;
background-color: #cb785c1a;
}
.prompt-icon {
height: 1.5rem;
width: 1.5rem;
background-color: rgb(var(--primary-light));
mask-repeat: no-repeat;
mask-position: center center;
}
.prompt-title {
color: rgb(31 41 55);
font-weight: 600;
}
.dark .prompt-title {
color: rgb(229 231 235);
}
.prompt-description {
margin-top: 0.25rem;
}
#prompts-container {
display: grid;
margin-top: 2.5rem;
}
@media (min-width: 640px) {
#category-select {
width: 16rem;
}
}
@media (min-width: 1024px) {
#prompts-container {
grid-template-columns: repeat(2, minmax(0, 1fr));
}
}
/\* Home page card styling \*/
.home-cards-custom {
display: grid;
grid-template-columns: repeat(3, 1fr);
grid-template-rows: repeat(2, auto);
gap: 1.5rem;
}
.home-cards-custom .card {
background: transparent;
border: 0.5px solid hsl(var(--border-300));
border-radius: 12px;
padding: 0.25rem;
}
/\* Responsive: change to 2 columns on tablet, single column on mobile \*/
@media (max-width: 1024px) {
.home-cards-custom {
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(3, auto);
}
}
@media (max-width: 768px) {
.home-cards-custom {
grid-template-columns: 1fr;
grid-template-rows: repeat(6, auto);
}
}
/\* Utility classes \*/
.relative {
position: relative;
}
.flex-1 {
flex: 1 1 0%;
}
/\* These styles mirror our design system (converted to plain CSS with Claude's help) from https://ui.product.ant.dev/button \*/
/\* Base button styles \*/
.btn {
position: relative;
display: inline-flex;
gap: 0.5rem;
align-items: center;
justify-content: center;
flex-shrink: 0;
min-width: 5rem;
height: 2.25rem;
padding: 0.5rem 1rem;
white-space: nowrap;
font-family: Styrene;
font-weight: 600;
border-radius: 0.5rem;
&:active {
transform: scale(0.985);
}
/\* Size variants \*/
&.size-xs {
height: 1.75rem;
min-width: 3.5rem;
padding: 0 0.5rem;
border-radius: 0.25rem;
font-size: 0.75rem;
gap: 0.25rem;
}
&.size-sm {
height: 2rem;
min-width: 4rem;
padding: 0 0.75rem;
border-radius: 0.375rem;
font-size: 0.75rem;
}
&.size-lg {
height: 2.75rem;
min-width: 6rem;
padding: 0 1.25rem;
border-radius: 0.6rem;
}
&:disabled {
pointer-events: none;
opacity: 0.5;
box-shadow: none;
}
&:focus-visible {
outline: none;
--tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
--tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(1px + var(--tw-ring-offset-width)) var(--tw-ring-color);
box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow);
}
/\* Primary variant \*/
&.primary {
font-weight: 600;
color: hsl(var(--oncolor-100));
background-color: hsl(var(--accent-main-100));
background-image: linear-gradient(
to right,
hsl(var(--accent-main-100)) 0%,
hsl(var(--accent-main-200) / 0.5) 50%,
hsl(var(--accent-main-200)) 100%
);
background-size: 200% 100%;
background-position: 0% 0%;
border: 0.5px solid hsl(var(--border-300) / 0.25);
box-shadow:
inset 0 0.5px 0px rgba(255, 255, 0, 0.15),
0 1px 1px rgba(0, 0, 0, 0.05);
text-shadow: 0 1px 2px rgb(0 0 0 / 10%);
transition: all 150ms cubic-bezier(0.4, 0, 0.2, 1);
&:hover {
background-position: 100% 0%;
background-image: linear-gradient(
to right,
hsl(var(--accent-main-200)) 0%,
hsl(var(--accent-main-200)) 100%
);
}
&:active {
background-color: hsl(var(--accent-main-000));
box-shadow: inset 0 1px 6px rgba(0, 0, 0, 0.2);
transform: scale(0.985);
}
}
/\* Flat variant \*/
&.flat {
font-weight: 500;
color: hsl(var(--oncolor-100));
background-color: hsl(var(--accent-main-100));
transition: background-color 150ms;
&:hover {
background-color: hsl(var(--accent-main-200));
}
}
/\* Secondary variant \*/
&.secondary {
font-weight: 600;
color: hsl(var(--text-100) / 0.9);
background-image: radial-gradient(
ellipse at center,
hsl(var(--bg-500) / 0.1) 50%,
hsl(var(--bg-500) / 0.3) 100%
);
border: 0.5px solid hsl(var(--border-400));
transition: color 150ms, background-color 150ms;
&:hover {
color: hsl(var(--text-000));
background-color: hsl(var(--bg-500) / 0.6);
}
&:active {
background-color: hsl(var(--bg-500) / 0.5);
}
}
/\* Outline variant \*/
&.outline {
font-weight: 600;
color: hsl(var(--text-200));
background-color: transparent;
border: 1.5px solid currentColor;
transition: color 150ms, background-color 150ms;
&:hover {
color: hsl(var(--text-100));
background-color: hsl(var(--bg-400));
border-color: hsl(var(--bg-400));
}
}
/\* Ghost variant \*/
&.ghost {
color: hsl(var(--text-200));
border-color: transparent;
transition: color 150ms, background-color 150ms;
&:hover {
color: hsl(var(--text-100));
background-color: hsl(var(--bg-500) / 0.4);
}
&:active {
background-color: hsl(var(--bg-400));
}
}
/\* Underline variant \*/
&.underline {
opacity: 0.8;
text-decoration-line: none;
text-underline-offset: 3px;
transition: all 150ms;
&:hover {
opacity: 1;
text-decoration-line: underline;
}
&:active {
transform: scale(0.985);
}
}
/\* Danger variant \*/
&.danger {
font-weight: 600;
color: hsl(var(--oncolor-100));
background-color: hsl(var(--danger-100));
transition: background-color 150ms;
&:hover {
background-color: hsl(var(--danger-200));
}
}
}

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

Getting started

Claude Code overview

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

##### Getting started

* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)

##### Build with Claude

* [Claude Code SDK](/en/docs/claude-code/sdk)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)

##### Deployment

* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)

##### Administration

* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)

##### Configuration

* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)

##### Reference

* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks](/en/docs/claude-code/hooks)

##### Resources

* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)

Getting started

# Claude Code overview

Copy page

Learn about Claude Code, Anthropic’s agentic coding tool that lives in your terminal and helps you turn ideas into code faster than ever before.

## [​](#get-started-in-30-seconds) Get started in 30 seconds

Prerequisites: [Node.js 18 or newer](https://nodejs.org/en/download/)

```
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Navigate to your project
cd your-awesome-project

# Start coding with Claude
claude

```

That’s it! You’re ready to start coding with Claude. [Continue with Quickstart (5 mins) →](/en/docs/claude-code/quickstart)

(Got specific setup needs or hit issues? See [advanced setup](/en/docs/claude-code/setup) or [troubleshooting](/en/docs/claude-code/troubleshooting).)

## [​](#what-claude-code-does-for-you) What Claude Code does for you

* **Build features from descriptions**: Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
* **Debug and fix issues**: Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
* **Navigate any codebase**: Ask anything about your team’s codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](/en/docs/claude-code/mcp) can pull from external datasources like Google Drive, Figma, and Slack.
* **Automate tedious tasks**: Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.

## [​](#why-developers-love-claude-code) Why developers love Claude Code

* **Works in your terminal**: Not another chat window. Not another IDE. Claude Code meets you where you already work, with the tools you already love.
* **Takes action**: Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](/en/docs/claude-code/mcp) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use *your* custom developer tooling.
* **Unix philosophy**: Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"` *works*. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
* **Enterprise-ready**: Use Anthropic’s API, or host on AWS or GCP. Enterprise-grade [security](/en/docs/claude-code/security), [privacy](/en/docs/claude-code/data-usage), and [compliance](https://trust.anthropic.com/) is built-in.

## [​](#next-steps) Next steps

[## Quickstart

See Claude Code in action with practical examples](/en/docs/claude-code/quickstart)[## Common workflows

Step-by-step guides for common workflows](/en/docs/claude-code/common-workflows)[## Troubleshooting

Solutions for common issues with Claude Code](/en/docs/claude-code/troubleshooting)[## IDE setup

Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)

## [​](#additional-resources) Additional resources

[## Host on AWS or GCP

Configure Claude Code with Amazon Bedrock or Google Vertex AI](/en/docs/claude-code/third-party-integrations)[## Settings

Customize Claude Code for your workflow](/en/docs/claude-code/settings)[## Commands

Learn about CLI commands and controls](/en/docs/claude-code/cli-reference)[## Reference implementation

Clone our development container reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer)[## Security

Discover Claude Code’s safeguards and best practices for safe usage](/en/docs/claude-code/security)[## Privacy and data usage

Understand how Claude Code handles your data](/en/docs/claude-code/data-usage)

Was this page helpful?

YesNo

[Quickstart](/en/docs/claude-code/quickstart)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Get started in 30 seconds](#get-started-in-30-seconds)
* [What Claude Code does for you](#what-claude-code-does-for-you)
* [Why developers love Claude Code](#why-developers-love-claude-code)
* [Next steps](#next-steps)
* [Additional resources](#additional-resources)