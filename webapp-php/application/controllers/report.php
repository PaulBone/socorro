<?php
/**
 * List, search, and show crash reports.
 */
class Report_Controller extends Controller {

    /**
     * List reports for the given search query parameters.
     */
    public function do_list() {
        $branch_data = $this->branch_model->getBranchData();
        $platforms   = $this->platform_model->getAll();

        $params = $this->getRequestParameters(array(
            'signature'    => '',

            'product'      => array(),
            'branch'       => array(),
            'version'      => array(),
            'platform'     => array(),

            'query_search' => 'signature',
            'query_type'   => 'contains',
            'query'        => '',
            'date'         => '',
            'range_value'  => '1',
            'range_unit'   => 'weeks',

            'do_query'     => FALSE
        ));

        cachecontrol::set(array(
            'etag'     => $params,
            'expires'  => time() + ( 60 * 60 )
        ));

        $reports = $this->common_model->queryReports($params);
        $builds  = $this->common_model->queryFrequency($params);

	if( count($builds) > 1){
	  $crashGraphLabel = "Crashes By Build";
	  $platLabels = $this->generateCrashesByBuild($platforms, $builds);
	  
	}else{
          $crashGraphLabel = "Crashes By OS";
	  $platLabels = $this->generateCrashesByOS($platforms, $builds);
	}

	$buildTicks = array();
	for($i = 0; $i  < count($builds); $i = $i + 1){
	  $buildTicks[] = array($i, date('m/d', strtotime($builds[$i]->build_date)));
	}
 
        $this->setViewData(array(
            'params'  => $params,
            'reports' => $reports,
            'builds'  => $builds,

            'all_products'  => $branch_data['products'],
            'all_branches'  => $branch_data['branches'],
            'all_versions'  => $branch_data['versions'],
            'all_platforms' => $platforms,

            'crashGraphLabel' => $crashGraphLabel,
            'platformLabels'  => $platLabels,
	    'buildTicks'      => $buildTicks
        ));
    }

    private function generateCrashesByBuild($platforms, $builds){
      $platLabels = array();
      foreach ($platforms as $platform){
	$plotData = array();
	for($i = 0; $i  < count($builds); $i = $i + 1){
	  $plotData[] = array($i, $builds[$i]->{"count_$platform->id"});
	}
	$platLabels[] = array("label" => substr($platform->name, 0, 3),
			      "data"  => $plotData,
			      "color" => $platform->color);
	}
      return $platLabels;
    }

    private function generateCrashesByOS($platforms, $builds){
        $platLabels = array();
        $plotData =   array();
	
        for($i = 0; $i < count($platforms); $i += 1){
          $platform = $platforms[$i];
          $plotData[$platform->id] = array($i, 0);
          for($j = 0; $j  < count($builds); $j = $j + 1){ 
            $plotData[$platform->id][1] += intval($builds[$j]->{"count_$platform->id"});
	  }
          $platLabels[] = array("label" => substr($platform->name, 0, 3),
				"data" => array($plotData[$platform->id]),
                                "color" => $platform->color);
        }
	return $platLabels;
    }

    /**
     * Fetch and display a single report.
     */
    public function index($uuid) {
        // Validate UUID to make sure there aren't any bullshit characters in it.
        if (!preg_match('/^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$/', $uuid) ) {
            return Event::run('system.404');
        }
 
        $report = $this->report_model->getByUUID($uuid);

        if (!$report) {
            if (!isset($_GET['p'])) {
                $this->priorityjob_model = new Priorityjobs_Model();
                $this->priorityjob_model->add($uuid);
            }
            return url::redirect('report/pending/'.$uuid);
        }

        cachecontrol::set(array(
            'etag'          => $uuid,
            'last-modified' => strtotime($report->date_processed)
        ));

        $this->setViewData(array(
            'report' => $report
        ));
    }

    /**
     * Wait while a pending job is processed.
     */
    public function pending($uuid) {
        if (!$uuid || !preg_match('/^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$/', $uuid)) {
            return Event::run('system.404');
        }

        $report = $this->report_model->getByUUID($uuid);
        if ($report) {
            $this->setAutoRender(FALSE);
            return url::redirect('report/index/'.$uuid);
        }

        $this->job_model = new Job_Model();
        $job = $this->job_model->getByUUID($uuid);

        $this->setViewData(array(
            'uuid' => $uuid,
            'job'  => $job
        ));
    }

    /**
     * Linking reports with ID validation.
     *
     * This method should not touch the database!
     */
    public function find() {
        $id = isset($_GET['id']) ? $_GET['id'] : '';
        $uuid = FALSE;

        if ($id) {
            $matches = array();
            $prefix = Kohana::config('application.dumpIDPrefix');
            if ( preg_match('/^('.$prefix.')?([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$/', $id, $matches) ) {
                $uuid = $matches[2];
            }
        }

        if ($uuid) {
            return url::redirect('report/index/'.$uuid);
        } else {
            return url::redirect('');
        }
    }
}
