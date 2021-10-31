query = '''
select
iuv.name, iuv.key, iuv.arch_db
from ir_model_data ird
left join ir_ui_view iuv on iuv.id = ird.res_id
where true
and ird.model = 'ir.ui.view'
and iuv.arch_fs != 'tx_website/views/views.xml'
and (
	iuv.arch_db ilike '%mailto:info@yourcompany.example.com%'
	or
	iuv.arch_db ilike '%tel:+1 (650) 691-3277%'
	or
	iuv.arch_db ilike '%tel:1 (650) 691-3277%'
) 
'''

import requests;
import scrapy;

url = 'http://localhost'
text = '''

<div class="oe_structure oe_structure_solo" id="oe_structure_header_hamburger_3">
	<section class="s_text_block" data-snippet="s_text_block" data-name="Text">
		<div class="container">
			<div class="row align-items-center">
				<!-- Separator -->
				<div class="col-lg-12">
					<div class="s_hr text-left pt16 pb16" data-name="Separator">
						<hr class="w-100 mx-auto" style="border-top-width: 1px; border-top-style: solid; border-color: var(--300);"/>
					</div>
				</div>
				<!-- Social -->
				<div class="col-lg-6 pb16">
					<div class="s_share text-left no_icon_color" data-name="Social Media">
						<h5 class="s_share_title d-none">Follow us</h5>
						<a href="/website/social/facebook" class="s_share_facebook" target="_blank">
							<i class="fa fa-facebook m-1"/>
						</a>
						<a href="/website/social/twitter" class="s_share_twitter" target="_blank">
							<i class="fa fa-twitter m-1"/>
						</a>
						<a href="/website/social/linkedin" class="s_share_linkedin" target="_blank">
							<i class="fa fa-linkedin m-1"/>
						</a>
						<a href="/website/social/instagram" class="s_share_instagram" target="_blank">
							<i class="fa fa-instagram m-1"/>
						</a>
					</div>
				</div>
				<!-- Contact -->
				<div class="col-lg-4 text-lg-right pb16">
					<i class="fa fa-1x fa-fw fa-envelope mr-2"/>
					<span>
						<a href="mailto:info@yourcompany.example.com">info@yourcompany.example.com</a>
					</span>
				</div>
				<div class="col-lg-2 text-lg-right pb16">
					<i class="fa fa-1x fa-fw fa-phone mr-2"/>
					<span class="o_force_ltr">
						<a href="tel:+1 (650) 691-3277">+1 (650) 691-3277</a>
					</span>
				</div>
			</div>
		</div>
	</section>
</div>
'''

response = scrapy.http.HtmlResponse(
	url = url,
	body = text,
	encoding = 'utf-8',
);

response.xpath("//a[@href='mailto:info@yourcompany.example.com']")
